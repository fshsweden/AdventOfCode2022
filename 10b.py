from collections import defaultdict
 
# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

with open('input-10.txt') as f:
    lines = [row.strip() for row in f]

screen = multi_dict(2, str)
for row in range(0, 6):
    for col in range(0, 40):
        screen[row][col] = ' '

def print_screen():
    for row in range(0, 6):
        for col in range(0, 40):
            print(screen[row][col], end='')
        print()

def draw_pixel(row, col):
    print(f"draw_pixel({row}, {col} sprite pos={X}")
    if col in range(X-1,X+2):
        screen[row][col] = '#'
    else:
        screen[row][col] = '.'


X=1
cycles = []

def cycle():
    global cycles
    cycles.append(X)

currow=0
curcol=0


def draw():
    global currow, curcol
    draw_pixel(currow, curcol)
    curcol += 1
    if curcol == 40:
        curcol = 0
        currow += 1

def execute_instruction(instr):
    global X

    if instr[0] == 'addx':
#       print(f"addx {instr[1]}")
        cycle()
        draw()
        cycle()
        draw()

        X += int(instr[1])

    if instr[0] == "noop":
        cycle()
        draw()

for line in lines:
    instr = line.split(' ')
    execute_instruction(instr)

#print(cycles)

ss=0
for ix in range(19,len(cycles),40):
    print(cycles[ix], cycles[ix] * (ix+1))
    ss += cycles[ix] * (ix+1)

print_screen()

print(ss)
