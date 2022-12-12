#
# This was the trickiest one so far.
# The key is the calc_supermodulo() function.
#
#

class Item:
    def __init__(self, worry_level) -> None:
        self.worry_level = int(worry_level)

    def __str__(self) -> str:
        return f"Item WL:{self.worry_level}"

    def __repr__(self) -> str:
        return f"Item WL:{self.worry_level}"

    def getWorryLevel(self):
        return self.worry_level

    def setWorryLevel(self, worry_level):
        self.worry_level = worry_level


class Monkey:
    def __init__(self) -> None:
        self.inspections = 0

    def __str__(self) -> str:
        return f"Monkey {self.id} has {self.starting_items}"

    def __repr__(self) -> str:
        return f"Monkey {self.id} has {self.starting_items}"

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def countInspection(self):
        self.inspections += 1

    def getInspections(self):
        return self.inspections

    def catch(self, item):
        self.items.append(item)

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
        if self.factor == "old":
            return self.factor
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
        self.iftrue = int(iftruemonkey)

    def getIffalsemonkey(self):
        return self.iffalse

    def setIffalsemonkey(self, iffalsemonkey):
        self.iffalse = int(iffalsemonkey)


class MonkeyController:

    def __init__(self) -> None:
        self.monkeys = {}
        self.load_monkeys()

    def load_monkeys(self):

        with open('input-11.txt') as f:
            lines = [row.strip() for row in f]
        
        lineno = 0  

        while lineno <= len(lines):
        
            monkey = Monkey()

            idline = lines[lineno].split(" ")
            id = idline[1].strip(":")
            
            monkey.setId(int(id))

            starting_items = lines[lineno+1].strip().split(":")[1]
            starting_items = starting_items.replace(" ", "")
            starting_items = starting_items.split(",")
            starting_items = [ Item(s) for s in starting_items]

            monkey.setItems(starting_items)

            operation_line = lines[lineno+2].split(":")[1].strip()
            factor = operation_line.split(" ")[4]
            operation = operation_line.split(" ")[3]

            if operation not in ["+", "*"]:
                raise "ERROR: operation not + or *"
                
            monkey.setOperation(operation)
            monkey.setFactor(factor)

            test = lines[lineno+3].split(":")[1]
            monkey.setTest(test)

            divisableby = int(test.split(" ")[3])
            monkey.setDivisableby(divisableby)

            iftrue = lines[lineno+4].split(":")[1]
            iftruemonkey = iftrue.split(" ")[4]
            monkey.setIftruemonkey(iftruemonkey)

            iffalse = lines[lineno+5].split(":")[1]
            iffalsemonkey = iffalse.split(" ")[4]
            monkey.setIffalsemonkey(iffalsemonkey)

            lineno += 7
            
            # monkey.print()

            self.monkeys[monkey.getId()] = monkey


    def calc_supermodulo(self):
        self.supermodulo = 1
        for m in self.monkeys:
            monkey = self.monkeys[m]
            self.supermodulo *= monkey.getDivisableby()
                
    def doRound(self):

        for m in self.monkeys:
            monkey = self.monkeys[m]

            #print(f"Monkey {m} starting with {monkey.getItems()}")

            for item in monkey.getItems():

                #print(f"Monkey {m} inspects item with WL: {item.getWorryLevel()}")
                monkey.countInspection()

                if monkey.getOperation() == "*":
                    old_worry_level = item.getWorryLevel()
                    if monkey.getFactor() == "old":
                        new_worry_level = item.getWorryLevel() * item.getWorryLevel()
                        #print(f"WL is multiplied by {old_worry_level} to {new_worry_level}")
                    else:
                        new_worry_level = item.getWorryLevel() * int(monkey.getFactor())
                        #print(f"WL is multiplied by {old_worry_level} to {new_worry_level}")

                elif monkey.getOperation() == "+":
                    if monkey.getFactor() == "old":
                        new_worry_level = item.getWorryLevel() + item.getWorryLevel()
                        #print(f"WL is increased by {old_worry_level} to {new_worry_level}")
                    else:
                        new_worry_level = item.getWorryLevel() + int(monkey.getFactor())
                        #print(f"WL is increased by {int(monkey.getFactor())} to {new_worry_level}")
                else:
                    raise "ERROR: operation not + or *"

                # new_worry_level = new_worry_level // 3
                # print(f"WL is divided by 3 to {new_worry_level}")
                item.setWorryLevel(new_worry_level % self.supermodulo)

                if new_worry_level % monkey.getDivisableby() == 0:
                    #print(f"Current worry level is divisible by {monkey.getDivisableby()}!")
                    #print(f"Item with worry level {item.getWorryLevel()} is thrown to {monkey.getIftruemonkey()}")
                    target_monkey = self.monkeys[monkey.getIftruemonkey()]
                    target_monkey.catch(item)
                else:
                    #print(f"Current worry level is NOT divisible by {monkey.getDivisableby()}!")
                    #print(f"Item with worry level {item.getWorryLevel()} is thrown to {monkey.getIffalsemonkey()}")
                    target_monkey = self.monkeys[monkey.getIffalsemonkey()]
                    target_monkey.catch(item)

                # remove items from starting_items
                monkey.setItems([])

    def print_monkeys(self):
        print(f"-- BEGIN -------------------------------------")
        for monkey_index in self.monkeys:
            monkey = self.monkeys[monkey_index]
            print(f"Monkey {monkey.getId()} has {monkey.getItems()}")
        print(f"-- END   -------------------------------------")

    def print_monkey_inspections(self):
        print(f"-- BEGIN -------------------------------------")
        for monkey_index in self.monkeys:
            monkey = self.monkeys[monkey_index]
            print(f"Monkey {monkey.getId()} inspected items {monkey.getInspections()} times")
        print(f"-- END   -------------------------------------")

def main():
    mc = MonkeyController()
    mc.load_monkeys()
    mc.calc_supermodulo()
    mc.print_monkeys()
    for round in range(10000):
        mc.doRound()
        if round == 0 or round == 19 or round % 1000 == 0:
            print(f"Round {round}")
            mc.print_monkey_inspections()

    mc.print_monkeys()
    mc.print_monkey_inspections()

if __name__ == "__main__":
    main()

