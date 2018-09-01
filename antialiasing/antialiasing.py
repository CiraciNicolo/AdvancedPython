import inspect
import re

def deepcopy(l):
    lc = list()
    for e in l:
        if type(e) is list:
            lc.append(deepcopy(e))
        else: lc.append(e)
    return lc

def delete(self):
    cframe = inspect.currentframe()
    bframe = cframe.f_back
    try:
        a = inspect.getframeinfo(bframe).code_context[0]
    except AttributeError: return
    m = re.search('([a-zA-Z][a-zA-Z0-9_]*)[ ]*=[ ]*(.*)$', a)
    bframe.f_locals[m.group(1)] = deepcopy(eval(m.group(2),bframe.f_locals))

class MetaAliasing(type):
    def __init__(meta, cls, bases, attr):
        return bases.__init__(meta, cls, bases, attr)
    def __new__(meta, cls, bases, attr):
        attr['__del__'] = delete
        return type.__new__(meta, cls, bases, attr)

list = MetaAliasing('list', (list,), dict(list.__dict__))
