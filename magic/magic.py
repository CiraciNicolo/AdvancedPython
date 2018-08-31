def magic(master):
    def dec(cls):
        class Shared: # Class container
            def __init__(self, *args, **kwargs):
                self.original = cls(*args, **kwargs)
                setattr(master, 'fathers', dict())
            def __getattr__(self, n):
                master.fathers[n] = self.original
                setattr(master, n, self.original.__class__.__dict__[n])
                return getattr(self.original, n)
            def __setattr__(self, n,v):
                if n == 'original': self.__dict__[n] = v
                setattr(self.original,n,v)
        return Shared
    return dec

def metagetattr(self, n):
    for v in self.fathers.items():
        if n in v[1].__dict__: return v[1].__dict__[n]
    raise AttributeError("Attribute «{}» doesn't exist".format(n))


class MetaMagic(type):
    def __new__(meta, cls, bases, attr):
        attr['__getattr__'] = metagetattr
        return type.__new__(meta, cls, bases, attr)

class Empty: pass

Empty = MetaMagic('Empty', (), dict(Empty.__dict__))
