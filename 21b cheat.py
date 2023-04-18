from collections import deque

class Monkey:
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }

    def __init__(self, name, value, monkey1=None, operation=None, monkey2=None):
        self.name = name
        self.value = value
        self.monkey1 = monkey1
        self.operation = operation
        self.monkey2 = monkey2

    def __repr__(self):
        return f"{self.name} {self.value} {self.monkey1} {self.monkey2}"

def read_input():
    with open("input21.txt") as file:
        params = []
        for line in file:
            name, *calculation = line.split()
            name = name.rstrip(":")
            if len(calculation) == 1:
                params.append((name, int(calculation[0])))
            else:
                params.append((name, None, *calculation))
    return params

def create_monkeys(params):
    return {param[0]: Monkey(*param) for param in params}

start = time()

# part 1
params = read_input()
monkeys = create_monkeys(params)
not_calculated = deque(monkeys.values())
while monkeys["root"].value is None:
    monkey = not_calculated.popleft()
    if monkey.value is not None:
        continue
    value1 = monkeys[monkey.monkey1].value
    value2 = monkeys[monkey.monkey2].value
    if value1 is not None and value2 is not None:
        monkey.value = Monkey.operations[monkey.operation](value1, value2)
        continue
    not_calculated.append(monkey)

print(int(monkeys["root"].value))

# part 2
monkeys = create_monkeys(params)
not_calculated = deque(monkeys.values())
root = monkeys["root"]

monkeys["humn"].value = None

while monkeys[root.monkey1].value is None and monkeys[root.monkey2].value is None:
    monkey = not_calculated.popleft()
    if monkey.value is not None or monkey.name == "humn":
        continue
    value1 = monkeys[monkey.monkey1].value
    value2 = monkeys[monkey.monkey2].value
    if value1 is not None and value2 is not None:
        monkey.value = Monkey.operations[monkey.operation](value1, value2)
        continue
    not_calculated.append(monkey)
    
if monkeys[root.monkey1].value is None:
    monkey = monkeys[root.monkey1]
    monkeys[root.monkey1].value = monkeys[root.monkey2].value
else:
    monkey = monkeys[root.monkey2]
    monkeys[root.monkey2].value = monkeys[root.monkey1].value

while monkeys["humn"].value is None:
    monkey1 = monkeys[monkey.monkey1]
    monkey2 = monkeys[monkey.monkey2]

    if monkey1.value is None and monkey2.value is None:
        raise ValueError("oh noes!")

    elif monkey1.value is None:
        if monkey.operation == "+":
            monkey1.value = monkey.value - monkey2.value
        elif monkey.operation == "-":
            monkey1.value = monkey.value + monkey2.value
        elif monkey.operation == "*":
            monkey1.value = monkey.value / monkey2.value
        elif monkey.operation == "/":
            monkey1.value = monkey.value * monkey2.value
        monkey = monkey1
    elif monkey2.value is None:
        if monkey.operation == "+":
            monkey2.value = monkey.value - monkey1.value
        elif monkey.operation == "-":
            monkey2.value = monkey1.value - monkey.value
        elif monkey.operation == "*":
            monkey2.value = monkey.value / monkey1.value
        elif monkey.operation == "/":
            monkey2.value = monkey1.value / monkey.value
        monkey = monkey2

print(int(monkeys["humn"].value))