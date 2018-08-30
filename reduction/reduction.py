class Value:
    def __init__(self, v): self._v = v
    def __str__(self): return self._v
    def __repr__(self): return self._v

    def eval(self): return int(self._v)
    def resolve(self): return self

class Operation:
    def __init__(self, op1, op, op2):
        self._op1 = op1
        self._op = op
        self._op2 = op2
    def __str__(self):
        return "({}{}{})".format(self._op1, self._op, self._op2)
    def __repr__(self):
        return "({}{}{})".format(self._op1, self._op, self._op2)

    def eval(self):
        return self._op._f(self._op1.eval(), self._op2.eval())
    def resolve(self):
        if isinstance(self._op1, Value) and isinstance(self._op2, Value):
            return Value(str(self.eval()))
        else:
            self._op1 = self._op1.resolve()
            self._op2 = self._op2.resolve()
            return self

class Operator:
    ops = {'+': lambda x,y: x+y, '*': lambda x,y: x*y, '-': lambda x,y: x-y, '/': lambda x,y: x//y}
    def __init__(self, op):
        self._op = op
        self._f = Operator.ops[op]
    def __str__(self): return self._op
    def __repr__(self): return self._op

class calculator:
    def __init__(self, expr):
        self._expr = expr
        self._ops, _ = self.extract()
    def __str__(self): return str(self._ops)
    def __repr__(self): return str(self._ops)
    def extract(self):
        def _extract(e, i):
            if i < len(e):
                if e[i] in '+*-/':
                    op1,i1 = _extract(e, i+1)
                    op2,i2 = _extract(e, i1+1)
                    return Operation(op1, Operator(e[i]), op2), i2
                return Value(e[i]), i
        return _extract(self._expr,0)
    def resolve(self):
        self._ops = self._ops.resolve()
        return self

def print_reduction(e):
    print(e)
    if type(e._ops) is not Value: print_reduction(e.resolve())
