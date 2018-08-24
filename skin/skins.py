import stack
from types import *

class Skins(type):
    def __new__(meta, classname, base, classdict):
        classdict['become'] = meta.become
        return super().__new__(meta, classname, base, classdict)

    def become(self, adds, removes):
        for a in adds:
            setattr(self, a.__name__, MethodType(a, self))
        for r in removes:
            if hasattr(self, r.__name__):
                delattr(self, r.__name__)
        pass

def pop(self):
    if self.top > 0:
        self.top -= 1
        self.data.pop()

def push(self, value):
    self.top += 1
    self.data.append(value)


stack = Skins('skins', (), dict(stack.stack.__dict__))
