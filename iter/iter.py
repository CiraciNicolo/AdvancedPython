class UpDownFile:

    def __init__(self, filename):
        self._fn = filename

    # reset all state every iterator is created
    def __iter__(self):
        self._c = []
        self._i = 0
        self._f = open(self._fn, 'r')
        return self

    def __next__(self):
        if len(self._c) == self._i:
            w = self.gw()
            self._c.append(w)
            self._i += 1
            return w
        else:
            self._i += 1
            return self._c[self._i-1]

    def ungetw(self):
        if self._i > 0:
            self._i -= 1

    # split[i] without builtins
    def gw(self):
        def _gw(w):
            c = self._f.read(1)
            if c == '': raise StopIteration # we reached the end file

            return _gw(w+c) \
                if c not in ' "\n\t.,;:?![]{}()' \
                else w if w!='' else _gw(w)

        return _gw('')
