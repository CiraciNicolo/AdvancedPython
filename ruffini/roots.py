import ruffini
import functools

def proots(self):
    x = self._coefficient[-1] # divisore di a_0
    x = -x if x<0 else x
    y = self._coefficient[0] # divisore di a_n
    y = -y if y<0 else y
    return sorted(set(p//q for p in [p for p in range(-x, x+1) if p!= 0 and x%p ==0] for q in [q for q in range(-y, y+1) if q!=0 and y%q ==0]))

def pfactors(self):
    divs = [Polynomial(1,-x) for x in self.proots() if (self % Polynomial(1,-x))==0] # tutti i polinomi per cui self//polinomio ha resto 0
    remainder = functools.reduce(Polynomial.__truediv__, [self]+divs)
    # se i fattori usati per dividere il polinomio danno un resto di grado 0 diverso da 1 oppure un resto di grado superiore allora inserisco anche quello
    return divs+([] if (remainder._n == 1 and remainder._coefficient[0]==1) else [remainder])

def roots(self):
    return [x for x in self.proots() if (self % Polynomial(1,-x))==0]


class ExtendedPolynomial(type):
    def __new__(m, c, s, d):
        d['proots'] = proots
        d['pfactors'] = pfactors
        d['roots'] = roots
        return type.__new__(m,c,s,d)

Polynomial = ExtendedPolynomial('ruffini.Polynomial', (), dict(ruffini.Polynomial.__dict__))
