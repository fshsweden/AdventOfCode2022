import sys
# "[D] [T] [V] [M] [J] [N] [F] [M] [G]"

parse = lambda line: (line[1],line[5],line[9],line[13],line[17],line[21],line[25],line[29],line[33])
test_parse = lambda line: (line[1],line[5],line[9])
#NUM_COLUMNS=3
NUM_COLUMNS=9

def data():
    with open('input-5.txt') as f:
        rows = [row.strip('\n') for row in f]
    return rows, 8

def test_data():
    data = []
    data.append("    [D]    ")
    data.append("[N] [C]    ")
    data.append("[Z] [M] [P]")
    data.append(" 1   2   3 ")

    data.append("move 1 from 2 to 1")
    data.append("move 3 from 1 to 3")
    data.append("move 2 from 2 to 1")
    data.append("move 1 from 1 to 2")

    return data, 3

mydata, rows = data()
d = mydata[:8]
instructions = mydata[10:]
stacks = [[],[],[],[],[],[],[],[],[]] # 9 stacks!

# data, x = test_data()
# d = data[:3]
# print(f"Data={d}")
# instructions = data[4:]
# print(f"Instructions={instructions}")
# stacks = [[],[],[]] # 3 stacks!



for i in d:
    stack_index=0
    for box in parse(i):  # test_parse
        if box == ' ':
            pass
        else:
            stacks[stack_index].insert(0, box)
        stack_index+=1



for s in range(len(stacks)):
    print(stacks[s])


def print_stack(index):
    print(f"Stack {index} has {len(stacks[index])} boxes", end=' ')
    for box in stacks[index]:
        print(box, end=' ')
    print()

for i in instructions:
    cmds = i.split(" ")
    numboxes = int(cmds[1])
    from_stack = int(cmds[3]) - 1
    to_stack = int(cmds[5]) - 1

    print("Before instruction " + str(cmds))
    for n in range(NUM_COLUMNS):
        print_stack(n)

    for n in range(numboxes):
        box = stacks[from_stack].pop()
        print("Popping ",box," from stack",from_stack+1)
        stacks[to_stack].append(box)
        print("Appended ",box," to stack",to_stack+1)
    
    print("After instruction " + str(cmds))
    for n in range(NUM_COLUMNS):
        print_stack(n)


