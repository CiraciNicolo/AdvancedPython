import sys

class TailRecursionException(Exception):
    def __init__(self, args, kwargs):
        self._args = args
        self._kwargs = kwargs

def tail_recursion(func):
    def optimize(*args, **kwargs):
        s = sys._getframe()
        if s.f_back and s.f_back.f_back and s.f_code == s.f_back.f_back.f_code:
            raise TailRecursionException(args, kwargs)
        else:
            while True:
                try:
                    return func(*args, **kwargs)
                except TailRecursionException as e:
                    args = e._args
                    kwargs = e._kwargs
    return optimize
