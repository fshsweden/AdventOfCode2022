from collections import defaultdict
 
# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

with open('input-10.txt') as f:
    lines = [row.strip() for row in f]

print(lines)

X=1
cycles = []

def cycle():
    global cycles
    cycles.append(X)

def execute_instruction(instr):
    global X
    if instr[0] == 'addx':
        print(f"addx {instr[1]}")
        cycle()
        cycle()
        X += int(instr[1])

    if instr[0] == "noop":
        cycle()

for line in lines:
    instr = line.split(' ')
    execute_instruction(instr)

print(cycles)

ss=0
for ix in range(19,len(cycles),40):
    print(cycles[ix], cycles[ix] * (ix+1))
    ss += cycles[ix] * (ix+1)

print(ss)
