def strip(s, c):
    if len(s) == 0: return ''
    return ('' if s[0] in c else s[0]) + strip(s[1::], c)

def reverse(s):
    if len(s) == 0: return ''
    return s[-1] + reverse(s[:-1])

def split(s, c):
    def _split(s, c, a, i):
        if len(s) == 0: return a
        if s[0] not in c:
            a[i] = a[i]+s[0]
        else:
            if len(a[i]) > 0 and len(s[1::]) > 0:
                a.append('')
                i+=1
        return _split(s[1::], c, a, i)
    return _split(s, c, [''],0)

def find(s, c):
    def _find(s,c,i):
        if len(s) == 0: return -1
        return i if s[0] in c else _find(s[1::], c, i+1)

    if find.state[2] != c or find.state[1] != s or find.state[0] == -1:
        find.state = [0, s, c]

    find.state[0] = _find(s[find.state[0]:], c, find.state[0]+1)
    return -1 if find.state[0] == -1 else find.state[0]-1

find.state = [0, '', '']
