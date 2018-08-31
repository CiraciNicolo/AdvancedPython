def even(g):
    for x in g:
        if x%2 == 0: yield x

def stopAt(g, n):
    for x in g:
        if x <= n: yield x
        else: break

def buffer(g, n):
    l = [x for x in g]
    for i in range(0, len(l), n):
        yield l[i:i + n]

def conditional(g, f):
    l = [next(g)]
    while True:
        l.append(next(g))
        if f(l[1]): yield l[0]
        l.pop(0)
