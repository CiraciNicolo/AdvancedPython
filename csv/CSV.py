from functools import *

def prettyCSV(filename):
    with open(filename, 'r') as f:
        l,m,ll=readCsv(f)
        ls = lines(l,m, ll)
        return reduce(lambda x,y: x+y, ls)

def lines(l,m,ml):
    return  ['-' * ml + '\n'] \
            + [reduce(lambda x,y: x+y, [('| ' if i == 0 else '') + e.strip() + (' ' * (m[i] - len(e))) + (' |\n' if i == len(m)-1 else ' | ') for i,e in enumerate(l[0])])] \
            + ['-' * ml + '\n'] \
            + [reduce(lambda x,y: x+y, [('| ' if i == 0 else '') + e.strip() + (' ' * (m[i] - len(e))) + (' |\n' if i == len(m)-1 else ' | ') for i,e in enumerate(ll)]) for ll in l[1::]] \
            +['-' * ml + '\n']

def readCsv(f):
    ls = [list(map(lambda e: e.strip().strip('"'), x)) for x in[x.split(';') for x in f.readlines()]]
    m = list(map(lambda x: len(x), [max(e, key=len) for e in zip(*[list(map(lambda x: x.strip(), x)) for x in [l for l in ls]])]))
    ll = sum(m) + (len(m) - 1) * 3 + 4
    return ls, m,ll
