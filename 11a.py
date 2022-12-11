with open('test-input-11.txt') as f:
    lines = [row.strip() for row in f]


class MonkeyController:
    def monkey_work(m):
        global monkeys

        monkey = monkeys[m]
        print(f"Monkey {m} starting with {monkey['starting_items']}")

        for item in monkey["starting_items"]:

            item = int(item)

            if monkey["operation"] == "*":
                if monkey["factor"] == "old":
                    worry_level = item * item
                else:
                    worry_level = item * int(monkey["factor"])
            elif monkey["operation"] == "+":
                if monkey["factor"] == "old":
                    worry_level = item + item
                else:
                    worry_level = item + int(monkey["factor"])

            print(f"worry_level is {worry_level} for item {item} and factor {monkey['factor']}")
            worry_level = worry_level // 3
            print(f"worry_level is {worry_level} after // 3")

            divis = monkey["divisableby"]

            if worry_level % monkey["divisableby"] == 0:
                print(f"Divisible by {divis}! passing {item} to {monkey['iftruemonkey']}")
                target_monkey = int(monkey["iftruemonkey"])
                catch(target_monkey, item)
            else:
                print(f"Not divisable by {divis}! passing {item} to {monkey['iffalsemonkey']}")
                target_monkey = int(monkey["iffalsemonkey"])
                catch(target_monkey, item)

            # remove items from starting_items
            monkey["starting_items"] = []

class Monkey:
    def __init__(self, id, 
        items, 
        operation, 
        test, 
        iftrue, 
        iffalse) -> None:

        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse

    def __str__(self) -> str:
        return f"Monkey {self.id} has {self.starting_items}"

    def __repr__(self) -> str:
        return f"Monkey {self.id} has {self.starting_items}"

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getItems(self):
        return self.items

    def setItems(self, items):
        self.items = items

    def getOperation(self):
        return self.operation

    def setOperation(self, operation):
        self.operation = operation

    def getTest(self):
        return self.test

    def setTest(self, test):
        self.test = test

    def getFactor(self):
        return self.factor

    def setFactor(self, factor):
        self.factor = factor

    def getDivisableby(self):
        return self.divisableby

    def setDivisableby(self, divisableby):
        self.divisableby = divisableby
    
    def getIftruemonkey(self):
        return self.iftrue

    def setIftruemonkey(self, iftruemonkey):
        self.iftrue = iftruemonkey

    def getIffalsemonkey(self):
        return self.iffalse

    def setIffalsemonkey(self, iffalsemonkey):
        self.iffalse = iffalsemonkey


class Item:
    def __init__(self, worry_level) -> None:
        self.worry_level = worry_level

    def __str__(self) -> str:
        return f"Item with worry level {self.worry_level}"

    def __repr__(self) -> str:
        return f"Item with worry level {self.worry_level}"

    def get_worry_level(self):
        return self.worry_level

    def set_worry_level(self, worry_level):
        self.worry_level = worry_level






def get_monkey_dicionary(lines):

    monkeys = {}

    done = False
    lineno = 0  

    while lineno <= len(lines):
    
        monkey = Monkey()

        idline = lines[lineno].split(" ")
        id = idline[1].strip(":")
        
        monkey.setId(int(id))

        starting_items = lines[lineno+1].strip().split(":")[1]
        starting_items = starting_items.replace(" ", "")
        starting_items = starting_items.split(",")
        starting_items = [ int(s) for s in starting_items]

        monkey.setItems(starting_items)

        # monkey["operation_line"] = lines[lineno+2].split(":")[1].strip()

        factor = monkey["operation_line"].split(" ")[4]
        operation = monkey["operation_line"].split(" ")[3]
        if operation not in ["+", "*"]:
            raise "ERROR: operation not + or *"
            
        monkey.setOperation(operation)
        monkey.setFactor(factor)

        test = lines[lineno+3].split(":")[1]
        monkey.setTest(test)

        divisableby = int(monkey["test"].split(" ")[3])
        monkey.setDivisableby(divisableby)

        iftrue = lines[lineno+4].split(":")[1]
        iftruemonkey = (monkey["iftrue"].split(" ")[4])
        monkey.setIftruemonkey(iftruemonkey)

        iffalse = lines[lineno+5].split(":")[1]
        iffalsemonkey = int(monkey["iffalse"].split(" ")[4])
        monkey.setIffalsemonkey(iffalsemonkey)

        lineno += 7
        
        monkey.print()

        monkeys[monkey["id"]] = monkey
    return monkeys

def catch(m, item):
    global monkeys
    monkeys[m]["starting_items"].append(item)

def print_monkeys(round, monkeys):
    print(f"-- BEGIN {round} -------------------------------------")
    for monkey_index in monkeys:
        monkey = monkeys[monkey_index]
        print(f"Monkey {monkey['id']} has {monkey['starting_items']}")
    print(f"-- END {round} -------------------------------------")


monkeys = get_monkey_dicionary(lines)

m = 0


print_monkeys(-1, monkeys)
for round in range(0,1):
    print(f"******************** Round {round}")
    for m in monkeys:
        monkey_work(m)
        print_monkeys(m, monkeys)
