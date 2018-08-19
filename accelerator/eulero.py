def pi_series():
    n,s,d,p = 4,0,1,0
    while True:
        p += ((-1) ** s) * 4 / d
        yield p
        s = (s+1)%2
        d += 2

def e_series():
    def fact(n):
        if n == 0: return 1
        else: return n * fact(n-1)
        
    d,p = 0,0
    while True:
        p += 1/fact(d)
        yield p
        d += 1

def euler_accelerator(g):
    n0 = next(g) # n-1
    n1 = next(g) # n
    n2 = next(g) # n+1
    while True:
        yield n2 - ((n2 - n1)**2)/(n0 - 2*n1 + n2)
        n0,n1,n2 = n1,n2,next(g)
