from types import *

def pre(a):
    def dec(func):
        def onCall(*args):
            a(func, args)
            return func(*args)
        onCall.__name__ = func.__name__
        return onCall
    return dec

def post(a):
    def dec(func):
        def onCall(*args):
            result = func(*args)
            a(func, args, result=result)
            return result
        onCall.__name__ = func.__name__
        return onCall
    return dec

def afterLog(func, args, result=None):
    print('** I\'ve called {}()'.format(func.__name__))

def beforeLog(func, args, result=None):
    print('** I\'m going to call {}()'.format(func.__name__))

def afterPostCondition(func, args, result=None):
    print('** the value the call should return is{}() :- {}'.format(func.__name__, result))

def beforePreCondition(func, args, result=None):
    print('*** {}() has been called with :- (\'{}\', {})'.format(func.__name__, args[1], args[2]))

def weaving(cls, pca):
    class AOPMeta(type):
        def __new__(cls, name, bases, attr):
            for k,v in attr.items():
                for n, f in pca:
                    if type(v) is FunctionType and k==n:
                        # Needs to reference attr[k] because in this way we get
                        # already decorated function (v != attr[k] if we have
                        # already decorated)
                        attr[k] = pre(f)(attr[k]) if 'before' in f.__name__ else post(f)(attr[k])
            attr['__dict__'] = attr
            return type.__new__(cls, name, bases, attr)

    return AOPMeta(cls.__name__, (), dict(cls.__dict__))
