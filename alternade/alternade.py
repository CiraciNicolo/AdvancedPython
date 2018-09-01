from itertools import *

def alternade(w, s):
    return [w[i::s] for i in range(s)]

def alternade_generator(fn, s):
    with open(fn, 'r') as f:
        l = [w.strip() for w in f.readlines()]
        ww = {k:[x for x in v] for k,v in groupby(l, lambda x: x[0])}
        for w in l:
            if len(w) >= s:
                aa = alternade(w, s)
                if all([a in ww[a[0]] for a in aa]):
                    yield w, aa
