def magic():
    a,b,c=5,5,1
    while True:
        yield a
        c += 2
        a += b*c
