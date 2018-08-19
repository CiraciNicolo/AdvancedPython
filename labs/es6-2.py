import traceback

def memoization(func):
    def wrapper(*args, **kwargs):
        if memoization.__dict__.get('state') is None:
            memoization.__dict__['state'] = {}

        try:
            return memoization.__dict__['state'][func.__name__][args[0]]
        except:
            r = func(*args, **kwargs)
            memoization.__dict__['state'].update({func.__name__: {args[0]:r}})
            return r
    return wrapper

def stack_trace(func):
    print("Stack for func {}".format(func.__name__))
    for line in traceback.format_stack():
        print(line.strip())
    return func

class MyMath(object):
    @staticmethod
    @stack_trace
    @memoization
    def fib(n):
        if n == 0: return 0
        elif n == 1: return 1
        else: return MyMath.fib(n-1)+MyMath.fib(n-2)

    @staticmethod
    @stack_trace
    @memoization
    def fact(n):
        if n == 0: return 1
        else: return n*MyMath.fact(n-1)

if __name__ == '__main__':
    print(MyMath.fib(6))
    print(MyMath.fact(4))
