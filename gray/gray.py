def _gray(n):
    if n == 1: return ["0","1"]
    else:
        l = _gray(n-1)
        return ["0"+g for g in l] + ["1"+g for g in l[::-1]]

def gray(i):
    for g in _gray(i): yield g

def memoization(func):
    def _memoization(*args):
        if not args in _memoization._cache.keys():
            _memoization._cache[args] = func(*args)
        else:
            print('### cached value for {} --> {}'.format(args, _memoization._cache[args]))
        return _memoization._cache[args]
    _memoization._cache = {}
    return _memoization

def mgray(i):
    global _gray # replace _gray globally
    _gray = memoization(_gray)
    return gray(i)
