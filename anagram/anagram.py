from functools import reduce

class Anagram:
    anagrams = {}

    def __init__(self):
        self.load()

    def __str__(self):
        l = {w[0]:sorted(w[1::], key=str.lower) for (k,w) in self.anagrams.items() if len(w[1::]) > 1}
        return reduce(lambda x,y: x+y, ["{:12} :- {}\n".format(k, ', '.join(w)) for k,w in l.items()])

    def load(self):
        with open('wordlist-anagram.txt') as f:
            for l in f.readlines():
                k = self._hash(l)
                if k in self.anagrams.keys():
                    self.anagrams[k] += [l.strip()]
                else: self.anagrams[k] = [l.strip()]

    def _hash(self, value):
        return ''.join(sorted(list(value.lower().strip())))

    def find(self, word):
        f = list(self.anagrams[self._hash(word)])
        f.remove(word)
        return ', '.join(f)

A = Anagram()

def anagrams():
    return str(A)

def anagram(word):
    return A.find(word)
