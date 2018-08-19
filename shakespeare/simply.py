import re
import string

def load_synonyms():
    def invert_dol(d):
        return dict((v, k) for k in d for v in d[k])

    with open("synonyms-list.txt", 'r') as file:
        r = re.compile("(\w+)[ ]+ : (.*)")
        d = {}
        for l in file.readlines():
            for w in [l.strip() for l in r.match(l).group(2).split(',')]:
                d[w] = r.match(l).group(1)
        return d

def replace_synonyms(s):
    sy = load_synonyms()
    r = []
    for w in s.split(' '):
        ws, ww = (w[-1:], w[:-1]) if w[-1:] in string.punctuation else ('', w)
        if ww.lower() in sy.keys():
            r.append(sy[ww].upper() + ws)
        else: r.append(ww + ws)
    return ' '.join(r)
