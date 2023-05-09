from copy import copy, deepcopy
from time import time,sleep
col = 9
row = 9
 
aliveCell = u'\u25A0' 
deadCell = u'\u25A1'
 
def create_box(cols,rows):
    new_box = [[deadCell for i in range (col)] for j in range(row)]
    return new_box
 
def radar_neighbors(B,x,y):
    counter = 0 
    L = (x - 1 + col) % col
    R = (x + 1 + col) % col 
    U = (y - 1 + row) % row 
    D = (y + 1 + row) % row 
    if(B[L][U] == aliveCell):
        counter += 1
    if (B[x][U] == aliveCell):
        counter += 1 
    if (B[R][U] == aliveCell):
        counter += 1
    if (B[L][y] == aliveCell):
        counter += 1 
    if (B[R][y] == aliveCell):
        counter += 1
    if (B[L][D] == aliveCell):
        counter += 1
    if (B[x][D] == aliveCell):
        counter += 1
    if (B[R][D] == aliveCell):
        counter += 1
    return counter
 
def box_change(B):
    tempB = deepcopy(B)
    for i in range(9):
        for j in range(9):
            ncount = radar_neighbors(B,j,i)
            if(B[j][i] == aliveCell):
                if(ncount < 2):
                    tempB[j][i] = deadCell
                elif (ncount == 2 or ncount == 3):
                    tempB[j][i] = aliveCell
                elif (ncount > 3):
                    tempB[j][i] = deadCell
            else:
                if (ncount == 3):
                    tempB[j][i] = aliveCell
    return tempB
 
def start_life():
    defaultBox = create_box(9,9)
    # Starting Config
    birth(defaultBox,2,5)
    birth(defaultBox,3,4)
    birth(defaultBox,3,6)
    birth(defaultBox,4,6)
    birth(defaultBox,4,4)
    print_box(defaultBox)
    print()
    gen1 = box_change(defaultBox)
    print_box(gen1)
    print()
    gen2 = box_change(gen1)
    print()
    print_box(gen2)
 
    
def print_box(printable):
    for y in printable:
        for x in y:
            print(x,end=' ')
        print()
 
def birth(B,r,c):
    B[r][c] = aliveCell
    return B
 
if __name__ == "__main__":
    start_life()
