import ABC
from types import *

# We can't directly use __call__ since it only intercept object creation.
# Instead we decorate every function of out target classes. It's also very
# important to reset the class type to our new metaobject.
class MetaTracer(type):
    def __new__(meta, name, bases, attr):
        c = []
        for k,v in attr.items():
            if type(v) is FunctionType:
                c.append(NodeDecorator(v,name))
                attr[k] = c[-1]
        no = type.__new__(meta, name, bases, attr)
        for d in c:
            d._func.__globals__[name] = no
        return no

class NodeDecorator:
    stack = ["main"]
    branches = []

    def __init__(self, func, cls):
        self._func = func
        self._classname = cls

    # __call__ is called for each method invocation, if we call the function we
    # travel trought the call stack and we get back when we return to the caller.
    # The branch operation is in place to detect this and create the correct
    # branches.
    def __call__(self, *args):
        NodeDecorator.push('"{}.{}({})"'.format(self._classname, self._func.__name__, *args))
        _ = self._func(*args)
        NodeDecorator.branch()
        NodeDecorator.pop()
        if(len(NodeDecorator.stack) == 1):
            NodeDecorator.saveToFile()

    @classmethod
    def push(self, value):
        self.stack.append(value)
    @classmethod
    def branch(self):
        if all([self.stack != sublist[:len(self.stack)] for sublist in self.branches]):
            self.branches.append(self.stack[:])
    @classmethod
    def pop(self):
        self.stack.pop()
    @classmethod
    def saveToFile(self):
        with open('cg.dot', 'w', encoding='utf-8') as o:
            o.write("strict digraph cg {\n")
            for e in self.branches:
                o.write('\t' + ' -> '.join(e) + "\n")
            o.write("}")

A = MetaTracer("A", (), dict(ABC.A.__dict__))
B = MetaTracer("B", (), dict(ABC.B.__dict__))
C = MetaTracer("C", (), dict(ABC.C.__dict__))
