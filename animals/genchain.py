from itertools import *

class AnimalChain:
    animals = {}

    def __init__(self):
        self.load()

    def load(self):
        with open('animals.txt') as f:
            self._l = [l.strip() for l in f.readlines()]
            self._w = {w:sorted([e for e in self._l if e[0] == w[-1] and e!=w]) for w in self._l}

    def chain(self, a):
        def _chain(a,ww):
            if len([w for w in self._w[a] if w not in ww]) == 0: return ww+[a]
            else: return self.ff([l for l in [_chain(w, ww+[a]) for w in self._w[a] if w not in ww] if l!=[]])
        r = sorted(self.ff([l for l in [_chain(w, [a]) for w in self._w[a] if self._w[a] != []] if l!=[]]))
        return r

    def ff(self, l):
        r = []
        for l1 in l:
            if all(isinstance(l2, str) for l2 in l1):
                r = r + [l1]
            else: r = r + self.ff(l1)
        r.sort()
        r = list(k for k,_ in groupby(r))
        return r

A = AnimalChain()

def genchain(a, *args):
    f = args[0] if len(args) > 0 else max
    l = A.chain(a)
    return f(l, key=len) if len(l) > 0 else [a]
