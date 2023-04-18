"""
This doesnt work.
I tried with a matrix, but I should have gone with a set() of tuples instead.
"""
from collections import defaultdict
import sys

# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

def checkSwapped(a,b):
    if a > b:
        return b,a
    else:
        return a,b

def draw(rowFrom,colFrom,rowTo,colTo):

    rowFrom,rowTo = checkSwapped(rowFrom,rowTo)
    colFrom,colTo = checkSwapped(colFrom,colTo)

    if rowFrom == rowTo: # same row, rowfrom == rowTo
        for col in range(colFrom, colTo+1):
            matrix[rowFrom][col] = '#'
    else: # same column: colFrom == colTo
        for row in range(rowFrom, rowTo+1):
            matrix[row][colFrom] = '#'

maxcol = 0
maxrow = 0
mincol = 9999
minrow = 9999

def checkMatrix(row,col):
    global mincol
    global minrow
    global maxcol
    global maxrow

    if row < 0:
        raise Exception(f"Row {row} is negative")
    if col < 0:
        raise Exception(f"Col {col} is negative")

    if row < minrow:
        minrow = row
    if col < mincol:
        mincol = col

    if row > maxrow:
        maxrow = row
    if col > maxcol:
        maxcol = col


def loadMatrix():
    global matrix
    global maxrow
    global maxcol

    with open('input-14.txt') as f:
        lines = [row.strip() for row in f]

    #
    # Se if any of the rows will extend the matrix
    #
    for line in lines:
        arr = line.split(' -> ')

        colFrom=None
        rowFrom=None

        for item in arr:
            pair = item.split(',')

            col = int(pair[0])
            row = int(pair[1])

            checkMatrix(row,col)

    print(f"Matrix dimensions: {minrow} {mincol} {maxrow} {maxcol}")

    #
    #
    #
    lengths = [len(line) for line in lines]
    #maxrow = len(lines)+1
    #maxcol = max(lengths)+1

    width = maxcol - mincol + 1
    height = maxrow - minrow + 1


    #
    # Create the matrix
    #
    matrix = multi_dict(2, str)

    #
    # 
    #     
    for row in range(0, maxrow + 1):
        for col in range(0, maxcol + 1):
            matrix[row][col] = '.'

    #
    #
    #
    for line in lines:
        arr = line.split(' -> ')
        #print(arr)

        colFrom=None
        rowFrom=None

        for item in arr:
            pair = item.split(',')

            if colFrom == None and rowFrom == None:
                # First!
                colFrom = int(pair[0])
                rowFrom = int(pair[1])
            else:
                colTo = int(pair[0])
                rowTo = int(pair[1])

                #print(f"Drawing from {rowFrom},{colFrom} to {rowTo},{colTo}")
                draw(rowFrom,colFrom-mincol,rowTo,colTo-mincol)

                colFrom = colTo
                rowFrom = rowTo
                
            col = int(pair[0])
            row = int(pair[1])

    matrix[0][6] = '+'
    # drawMatrix()

    
def drawMatrix():    
    global matrix
    for row in matrix:
        print(row, end=': ')
        for col in matrix[row]:
            print(matrix[row][col], end='')
        print(' ')

def fall(row,col):
    global matrix

    # if next row is empty, fall
    if col < 0:
        return False # Not at rest
    else:
        if matrix[row+1][col] == '.':
            return fall(row+1,col)
        else:
            # if next row is not empty, check if we can fall diagonally left
            if matrix[row+1][col-1] == '.' or col == 0:
                return fall(row+1,col-1)
            # if next row is not empty, check if we can fall diagonally right
            elif matrix[row+1][col+1] == '.':
                return fall(row+1,col+1)
            else:
                # we can't fall anymore, so stop
                matrix[row][col] = 'O'
                return True # at rest
    
    

def dropSandUnit():
    global matrix

    row = 0
    col = 6

    count = 0
    rest = fall(row,col)
    while rest == True:
        count += 1
        rest = fall(row,col)

    print(f"{count} sand units dropped.")


def main():
    loadMatrix()
    dropSandUnit()
    drawMatrix()

if __name__ == "__main__":
    main()
