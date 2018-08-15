from types import FunctionType

def decorate(func):
    def onCall(*args, **kwargs):
        self = args[0]
        for a,b in list(zip(func.__code__.co_varnames, args))[1:]:
            self.__dict__[a] = b
        return func(*args, **kwargs)
    return onCall

class AutoInit(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:
                classdict[attr] = decorate(attrval)
        return type.__new__(meta, classname, supers, classdict)
