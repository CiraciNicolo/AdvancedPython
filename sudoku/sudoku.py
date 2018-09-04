from itertools import *

def grid():
    all_permutations = list(product(range(0,24),range(0,24),range(0,24),range(0,24))) # 4*3*2*1 valori per riga, 4 righe
    accepted_values = list(permutations(range(1,5))) # 1<=x<5
    for i in range(0, len(all_permutations)):
        # all_permutations contains all the combinations of the possibile 4 values in this row
        # instead accepted_values contains all the permutations of the numbers 1,2,3,4
        g = [accepted_values[all_permutations[i][j]] for j in range(0,4)]
        yield g
    raise StopIteration

def sudoku():
    s = grid()
    while True:
        c = next(s)
        if check_columns(c) and check_squares(c): yield c

def check_columns(c):
    for j in range(0,4):
        if len({c[i][j] for i in range(0,4)})<4: return False
    return True

def check_squares(c):
    for offx in [0,2]:
        for offy in [0,2]:
            if len({c[x+offx][y+offy] for x in range(0,2) for y in range(0,2)})<4: return False
    return True
