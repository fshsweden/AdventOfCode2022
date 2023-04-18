from collections import defaultdict

def nested_dict(n, type):
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: nested_dict(n-1, type))

current_row = 0
current_col = 0
numrows = 0
numcols = 0

def getCommands(str):
    n = 3 # chunk length
    chunks = []
    i = 0
    first = True

    while i < len(str):
        print(f"processing({str[i:]})")
        if first:
            cmd = ""
            first = False
            i-=1
        else:
            cmd = str[i]

        if str[i+1:i+1+1].isnumeric() and (i+2 < len(str) and str[i+2:i+2+1].isnumeric()):
            num = int(str[i+1] + str[i+2])
            i = i+3
            print(f"Adding chunk: {num} {cmd}")
            chunks.append((num, cmd))
        else:
            if str[i+1:i+1+1].isnumeric() and (i+1 < len(str)):
                num = int(str[i+1])
                i = i+2
                print(f"Adding chunk: {num} {cmd}")
                chunks.append((num, cmd))
            
    return chunks


def printMap(map):
    for row in range(numrows):
        for col in range(numcols):
            print(map[row][col], end='')
        print()

def load():
    global numrows
    global numcols
    map = nested_dict(2, str)

    with open("test-input-22.txt") as f:
        input_lines = f.read().splitlines()

    # print(input_lines[:-1])
    # print(input_lines[:-2])

    row = 0
    for line in input_lines[:-2]:
        col = 0
        for ch in line:
            map[row][col] = ch
            col += 1
        row += 1

    cmds = input_lines[-1]

    numrows = row
    numcols = col

    return map, cmds

NONE=0
UP=1
RT=2
DN=3
LF=4

def nextup(row,col):
    global map
    if row-1 >= 0:
        row -= 1
        ch = map[row][col]
    else:
        ch = map[numrows-1][col]

    return ch

def nextdn(row,col):
    global map
    if row+1 < numrows-1:
        row += 1
        ch = map[row][col]
    else:
        ch = map[0][col]

    return ch

def nextleft(row,col):
    global map
    if col-1 >= 0:
        col -= 1
        ch = map[row][col]
    else:
        ch = map[row][numcols-1]

    return ch

def nextright(row, col):
    global map
    if col+1 < numcols-1:
        col += 1
        ch = map[row][col]
    else:
        ch = map[row][0]
    
    return ch


def stepup(row):
    global map
    if row-1 >= 0:
        row -= 1
        return row
    else:
        return numrows-1

def stepdn(row):
    global map
    if row+1 < numrows-1:
        row += 1
        return row
    else:
        return 0

def stepleft(col):
    global map
    if col-1 >= 0:
        col -= 1
        return col
    else:
        return numcols-1

def stepright(col):
    global map
    if col+1 < numcols-1:
        col += 1
        return col
    else:
        return 0


def walk(facing:int, turn:str, row:int, col:int):
    wall = False

    print(f"Facing: {facing} Turn: {turn} Row: {row} Col: {col}")

    if turn == "":
        pass
    else:
        if facing == UP:
            if turn == "L":
                facing = LF
            else:
                facing = RT
        else:
            if facing == DN:
                if turn == "L":
                    facing = RT
                else:
                    facing = LF
            else:
                if facing == LF:
                    if turn == "L":
                        facing = DN
                    else:
                        facing = UP
                else:
                    if facing == RT:
                        if turn == "L":
                            facing = UP
                        else:
                            facing = DN
                    else:
                        raise Exception("Invalid direction")
    
    print(f"Facing Now: {facing}")

    if facing == UP:
        while True:
            if nextup(row,col) == "#":
                wall = True
                break
            row = stepup(row)
            if map[row][col] != ' ':
                break
    else:
        if facing == DN:
            while True:
                if nextdn(row,col) == "#":
                    wall = True
                    break
                row = stepdn(row)
                if map[row][col] != ' ':
                    break
        else:
            if facing == LF:
                while True:
                    if nextleft(row,col) == "#":
                        wall = True
                        break
                    col = stepleft(col)
                    if map[row][col] != ' ':
                        break
            else:
                if facing == RT:
                    while True:
                        if nextright(row,col) == "#":
                            wall = True
                            break
                        col = stepright(col)
                        if map[row][col] != ' ':
                            break
                else:
                    raise Exception("Invalid direction")
    return facing,row,col,wall

def find_start(map):
    row = col = 0
    facing,row,col,wall = walk(RT, "", row, col)
    return row, col

map,cmds = load()
printMap(map)

row,col = find_start(map)
print(f"Start: ({row},{col})")

for cmd in getCommands(cmds):
    print("Executing ", cmd)
    facing = RT

    first = True
    for i in range(cmd[0]):
        # Bug TURN SHOULD BE "L/R" on first, then NONE
        # But NOT ON FIRST MOVE!!!!!!!!
        facing,row,col,wall = walk(facing, cmd[1] if first else "", row, col)
        first = False
        print(f"Got to: ({facing} {row},{col}) {map[row][col]}")
        if wall:
            print("Hit a wall")
            break

# print(col, row)
# col, row = walk(RT, col, row)
# print(col, row)
# col, row = walk(DN, col, row)
# print(col, row)
