from threading import *

class asynchronous:
    def __init__(self, func):
        self._f = func
        self._r = []
        self._w = lambda *args, **kwargs: self._r.append(func(*args, **kwargs))

    def start(self, *args):
        self._r = []
        t = Thread(target=self._w, args=args)
        t.start()
        return asynchronous.Result(self._r, t)

    class Result:
        def __init__(self, result, thread):
            self._r = result
            self._t = thread

        def is_done(self):
            return not self._t.is_alive()

        def get_result(self):
            if not self.is_done():
                raise asynchronous.NotYetDoneException('the call has not yet completed its task')
            else:
                if not hasattr(self, 'result'):
                    self.result = self._r.pop()
                return self.result

    class NotYetDoneException(Exception):
        def __init__(self, message): self.message = message
