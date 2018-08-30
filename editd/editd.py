import itertools
import json, os.path

class Chain:
    def __init__(self):
        with open('wordlist-7.txt', 'r') as f:
            self._l = [x.strip() for x in f.readlines()]
            if os.path.exists('cache.json'):
                with open('cache.json', 'r') as file:
                    self._w = json.loads(file.read())
            else: ## cache to speed up testing
                self._w = {w:sorted([e for e in self._l if self.cd(w,e)]) for w in self._l}
                with open('cache.json', 'w') as file:
                    file.write(json.dumps(self._w))
                    print("written!")

    def cd(self, a, b):
        return list(itertools.tarmap(lambda x,y: x==y, zip(a, b))).count(False) == 1

    def chain(self,a,b):
        def _chain(a, b, ww):
            if a == b: return ww + [a] # we reached the end
            else: return self.flat([l for l in [_chain(w, b, ww+[a]) for w in self._w[a] if w not in ww] if l!=[]]) # flat is not required but welcome, because the recursione create a lot of sublists
        r = sorted(self.flat([l for l in [_chain(w, b, [a]) for w in self._w[a] if self._w[a] != []] if l!=[]])) # all list that can be generated from affine words
        return ''.join(["{}\n".format(l) for l in r])

    def flat(self, l):
        r = []
        for l1 in l:
            if all(isinstance(l2, str) for l2 in l1):
                r = r + [l1]
            else: r = r + self.flat(l1)
        return r

C = Chain()

def chain(a,b):
    return C.chain(a,b)
