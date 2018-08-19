import math

def trialdivision(n):
    print("Trial-Division's Primality Test", end='\t')
    d = [x for x in range(1, n+1) if n%x == 0]
    return len(d) == 2

def lucaslehmer(n):
    def _lucaslehmer(m):
        i = 0
        s = 4
        while i != m:
            i += 1
            s = s**2 - 2
        return s

    print("Lucas-Lehmer's Primality Test", end='\t')
    m = math.log(n+1, 2) - 2
    return _lucaslehmer(m) % n == 0

def littlefermat(n):
    print("Little Fermat's Primality Test", end='\t')
    # L'operazione generara solo numeri congrui a 1 se n è primo, dunque la lunghezza del set sarà 1.
    # Inoltre vista la grandezza del numero da testare, prendo come limite inferiore di a la sqrt(n)
    return len(set([pow(a,(n-1),n) for a in range(int(math.sqrt(n)), n)])) == 1

def is_prime(n):
    if 0 < n <= 10000: return trialdivision(n)
    elif 10000 < n <= 524280: return lucaslehmer(n)
    else: return littlefermat(n)
