import math

def far(s):
    ops = {'w': (lambda a,b,c: (a-c,b)), 'e': (lambda a,b, c: (a+c,b)), 'n': (lambda a,b, c: (a,b+c)), 's': (lambda a,b, c: (a,b-c))}
    def _far(st, r):
        if len(st) == 0: return r
        else: return _far(st[1::], ops[st[0][0]](*r, int(st[0][1])))

    s = [(c[0], c[1]) for c in [s[i:i+2] for i in range(0, len(s), 2)]]
    r = _far(s, (0,0))
    return math.sqrt(r[0]**2 + r[1]**2)
