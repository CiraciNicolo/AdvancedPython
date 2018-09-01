from account import *
import types
import inspect

class AccountHole(type):
    def __new__(meta, clsname, bases, attr):
        for k,v in attr.items():
            if type(v) is types.FunctionType and k not in ['__init__', 'balance']:
                attr[k] = AccountHole.wrapper(v)
        return type.__new__(meta, clsname, bases, attr)

    @staticmethod
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            frame = inspect.currentframe()
            s = '## At the {} Has been requested a «{}» on the account {} owned by Walter for {}€.'
            print(s.format(frame.f_back.f_locals['self'].idn, func.__name__, args[0].number, args[1]))
            return func(*args, **kwargs)
        return _wrapper

Account = AccountHole('Account', (), dict(Account.__dict__))
