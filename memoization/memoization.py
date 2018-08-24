from random import *

def memoization(func):
    def _memoization(*args):
        if args in _memoization._cache.keys():
            print('### cached value for {} --> {}'.format(args, _memoization._cache[args]))
        else:
            _memoization._cache[args] = func(*args)
        return _memoization._cache[args]
    _memoization._cache = {}
    return _memoization

@memoization
def sum(x,y):
    return x if y == 0 else sum(x+1,y-1)

@memoization
def fibo(n):
    return n if n <= 1 else fibo(n-1) + fibo(n-2)
@memoization
def fact(n):
    return n if n == 1 else n*fact(n-1)

def mul(n,m):
    def _mul(c,m,t):
        return c if m == t else _mul(c+n, m, t+1)
    return _mul(n,m,1)
