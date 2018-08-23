def case(values):
    def decorate(func):
        func.__conditions = values
        return func
    return decorate

class Switch:
    def __init__(self):
        self.__cases = {}
        # we cannot use __dict__ since we need to introspect the subclasses in
        # the module
        f = [(e, getattr(e, '__conditions')) for e in [getattr(self, e) for e in dir(self) if getattr(self, e, None) is not None] if hasattr(e, '__conditions')]
        for e, v in f:
            if isinstance(v, tuple) or isinstance(v, list):
                for t in v:
                    self.__cases[t] = e
            else:
                self.__cases[v] = e

    def match(self, value):
        try:
            return self.__cases[value]
        except:
            return self.__cases["default"]
