from itertools import *
from functools import *

class TooHighOrderDivisorException(Exception): pass

class Polynomial():

    def __init__(self, *args):
        self._coefficient = args
        self._n = len(args)

    def __repr__(self):
        def format(c):
            return ("{:+d}" if isinstance(c, int) else "{:+4.2f}").format(c)
        def exponenent(i):
            return '' if i<=1 else (chr(176+i) if i<4 else chr(8304+i))
        def term(c, i):
            if c == 0: return ''
            if i == 0: return format(c)
            return "-x{}".format(exponenent(i)) if c == -1 else ("+x{}".format(exponenent(i)) if c == +1 else "{}x{}".format(format(c), exponenent(i)))
        s = ''.join([term(c,len(self._coefficient)-i-1) for (i,c) in enumerate(self._coefficient)])
        return s if len(s) > 0 and s[0] == "-" else s[1::]

    def monomials(self):
        return [Polynomial(*([self._coefficient[i]] + [0]*(self._n - 1 - i))) for i in range(0, self._n) if self._coefficient[i] != 0]

    def __add__(self, other):
        return Polynomial(*[c1+c2 for (c1,c2) in list(zip_longest(self._coefficient[::-1], other._coefficient[::-1], fillvalue=0))][::-1])

    def __sub__(self, other):
        return Polynomial(*[c1-c2 for (c1,c2) in list(zip_longest(self._coefficient[::-1], other._coefficient[::-1], fillvalue=0))][::-1])

    def __lshift__(self, other):
        return Polynomial(*([other._coefficient[0]*self._coefficient[i] for i in range (0, self._n)] + (other._n-1)*[0]))

    def __mul__(self, other):
        return reduce(lambda x,y: x+y, [self<<m for m in other.monomials()])

    def __truediv__(self, other):
        return self.ruffini(other)[0]

    def __mod__(self, other):
        return self.ruffini(other)[1]

    def ruffini(self, other):
        if other._n > 2: raise TooHighOrderDivisorException("ERROR!!! The divisor {} is too high order! It should be one!".format(other))
        r = -other._coefficient[-1]//other._coefficient[0]
        q = [self._coefficient[0]]
        for a in self._coefficient[1:]:
            q += [q[-1]*r+a]
        return Polynomial(*q[:-1]),q[-1]*other._coefficient[0]
