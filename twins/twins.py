import inspect
from types import *

def twinsinit(a):
    def _twinsinit(self, *args):
        for i,l in a:
            i(self, *args[:l])
            args = args[l:]
    return _twinsinit

def twinscalls(f):
    def _twinscalls(self, name):
        if name in f: return lambda *args: f[name](self, *args)
    return _twinscalls

def Twins(cl):
    a = [(c.__dict__['__init__'], len(inspect.getfullargspec(c.__dict__['__init__']).args[1::])) for c in cl]
    f = {k:v for c in cl for k,v in c.__dict__.items() if type(v) is FunctionType and k != '__init__'}
    class MetaTwins(type):
        def __new__(cls, name, bases, attr):
            attr['__init__'] = twinsinit(a)
            attr['__getattr__'] = twinscalls(f)
            return type.__new__(cls, name, bases, attr)
    return MetaTwins
