from collections import defaultdict
 
# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

monkeys = {}

class Monkey:
    def __init__(self, name, **kwargs):
        self.visited = False
        self.name = name
        for k,v in kwargs.items():
            setattr(self, k, v)

    def connect(self):
        if hasattr(self, 'shout'):
            pass
        else:
            self.monkey1 = monkeys[self.monkeyname1]
            self.monkey2 = monkeys[self.monkeyname2]

    def getvalue(self):
        if hasattr(self, 'shout'):
            return self.shout
        else:
            if self.visited:
                return self.shout
            else:
                self.visited = True
                if self.operation == '+':
                    self.shout = self.monkey1.getvalue() + self.monkey2.getvalue()
                    return self.shout
                elif self.operation == '*':
                    self.shout = self.monkey1.getvalue() * self.monkey2.getvalue()
                    return self.shout
                elif self.operation == '-':
                    self.shout = self.monkey1.getvalue() - self.monkey2.getvalue()
                    return self.shout
                elif self.operation == '/':
                    self.shout = self.monkey1.getvalue() / self.monkey2.getvalue()
                    return self.shout
                else:
                    raise Exception(f"Unknown operation {self.operation}")


    def __repr__(self):
        if hasattr(self, 'shout'):
            return f"Monkey({self.name}, {self.shout})"
        else:
            return f"Monkey({self.name}, {self.monkeyname1}, {self.operation}, {self.monkeyname2})"
        

def data():
    global monkeys

    with open('input-21.txt') as f:
        lines = [row.strip() for row in f]
    for line in lines:

        x = line.split(":")
        name = x[0]
        formula = x[1].strip()

        print(f"Monkey {name} is {formula}")

        try:
            shout = int(formula)

            monkeys[name] = Monkey(name, shout=shout)
        except Exception as e:
            monkeyname1 = formula.split(" ")[0].strip()
            operation = formula.split(" ")[1].strip()
            monkeyname2 = formula.split(" ")[2].strip()

            print(f"Monkey {name} is {monkeyname1} {operation} {monkeyname2}")
            monkeys[name] = Monkey(name, monkeyname1=monkeyname1, operation=operation, monkeyname2=monkeyname2)




def main():
    data()
    for monkeyname in monkeys:
        print(f"Monkey {monkeyname} is {monkeys[monkeyname]}")
        monkeys[monkeyname].connect()

    print(monkeys["root"].getvalue())

if __name__ == "__main__":
    main()
