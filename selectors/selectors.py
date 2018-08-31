from types import *

def private(*fields):
    def decorator(cls):
        class PrivateWrapper:
            def __init__(self, *args, **kwargs):
                self.wrapped = cls(*args, **kwargs)
                self.fields = list(fields)
            def __getattr__(self, name):
                if name in list(fields):
                    raise TypeError('private attribute fetch: ' + name)
                else: return getattr(self.wrapped, name)
            def __setattr__(self, name, value):
                if name == 'wrapped': self.__dict__[name] = value
                if name in list(fields):
                    raise TypeError('private attribute change: ' + name)
                else: setattr(self.wrapped, name, value)
        return PrivateWrapper
    return decorator

def selectors(methods):
    def decorator(cls):
        class SelectorWrapper:
            def __init__(self, *args, **kwargs):
                self.wrapped = cls(*args, **kwargs)
                w = {'get': lambda n: lambda s: s.__dict__[n], 'set': lambda n: lambda s,v: s.__dict__.update({n:v})}
                for t, fl in methods.items():
                    for f in fl:
                        if f not in self.wrapped.fields:
                            raise TypeError('attempt to add a selector for a non private attribute: {}'.format(f))
                        else:
                            self.wrapped.wrapped.__dict__['{}{}'.format(t, f.capitalize())] = MethodType(w[t](f), self.wrapped.wrapped)
            def __getattr__(self, name):
                return getattr(self.wrapped, name)
            def __setattr__(self, name, value):
                if name == 'wrapped': self.__dict__[name] = value
                else: setattr(self.wrapped, name, value)
        return SelectorWrapper
    return decorator
