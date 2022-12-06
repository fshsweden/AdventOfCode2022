import sys

stacks = []

def print_stack(index):
    print(f"Stack {index} has {len(stacks[index])} boxes", end=' ')
    for box in stacks[index]:
        print(box, end=' ')
    print()

def execute_instructions(instructions, stacks, num_columns):
    for i in instructions:
        cmds = i.split(" ")
        numboxes = int(cmds[1])
        from_stack = int(cmds[3]) - 1
        to_stack = int(cmds[5]) - 1

        print("Before instruction " + str(cmds))
        for n in range(num_columns):
            print_stack(n)

        boxes = stacks[from_stack][-numboxes:]
        del stacks[from_stack][-numboxes:]
        print("Popping ",numboxes, boxes," from stack",from_stack)
        stacks[to_stack] = stacks[to_stack] + boxes
        print("Appended ",boxes," to stack",to_stack)
        
        print("After instruction " + str(cmds))
        for n in range(num_columns):
            print_stack(n)


def solve_test():
    global stacks
    test_parse = lambda line: (line[1],line[5],line[9])
    NUM_COLUMNS=3

    data = []
    data.append("    [D]    ")
    data.append("[N] [C]    ")
    data.append("[Z] [M] [P]")
    data.append(" 1   2   3 ")

    data.append("move 1 from 2 to 1")
    data.append("move 3 from 1 to 3")
    data.append("move 2 from 2 to 1")
    data.append("move 1 from 1 to 2")

    d = data[:3]
    print(f"Data={d}")
    instructions = data[4:]
    print(f"Instructions={instructions}")
    stacks = [[],[],[]] # 3 stacks!

    for i in d:
        stack_index=0
        for box in test_parse(i):
            if box == ' ':
                pass
            else:
                stacks[stack_index].insert(0, box)
            stack_index+=1

    execute_instructions(instructions, stacks, NUM_COLUMNS)

def solve():   
    global stacks
    parse = lambda line: (line[1],line[5],line[9],line[13],line[17],line[21],line[25],line[29],line[33])
    NUM_COLUMNS=9

    with open('input-5.txt') as f:
        rows = [row.strip('\n') for row in f]

    mydata = rows
    d = mydata[:8]
    instructions = mydata[10:]
    stacks = [[],[],[],[],[],[],[],[],[]] # 9 stacks!

    for i in d:
        stack_index=0
        for box in parse(i):  # test_parse
            if box == ' ':
                pass
            else:
                stacks[stack_index].insert(0, box)
            stack_index+=1

    execute_instructions(instructions, stacks, NUM_COLUMNS)


#solve_test()
solve()

print("Answer:", end='')
for s in stacks:
    print(s[-1], end='')
print()