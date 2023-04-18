from collections import defaultdict
 
import sys

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
                elif self.operation == '=':
                    self.shout = self.monkey1.getvalue() - self.monkey2.getvalue()
                    v1 = self.monkey1.getvalue()
                    v2 = self.monkey2.getvalue()
                    if v1 == v2:
                        print("*** SUCCESS ***")
                    else:
                        print("*** FAIL ***")
                    return v1 - v2
                else:
                    raise Exception(f"Unknown operation {self.operation}")


    def __repr__(self):
        if hasattr(self, 'shout'):
            return f"Monkey({self.name}, {self.shout})"
        else:
            return f"Monkey({self.name}, {self.monkeyname1}, {self.operation}, {self.monkeyname2})"
        

def data():
    global monkeys

    monkeys = {}

    with open('input-21.txt') as f:
        lines = [row.strip() for row in f]
    for line in lines:

        x = line.split(":")
        name = x[0]
        formula = x[1].strip()

        # print(f"Monkey {name} is {formula}")

        try:
            shout = int(formula)

            monkeys[name] = Monkey(name, shout=shout)
        except Exception as e:
            monkeyname1 = formula.split(" ")[0].strip()
            operation = formula.split(" ")[1].strip()
            monkeyname2 = formula.split(" ")[2].strip()

            # print(f"Monkey {name} is {monkeyname1} {operation} {monkeyname2}")
            monkeys[name] = Monkey(name, monkeyname1=monkeyname1, operation=operation, monkeyname2=monkeyname2)


# 1     => 53857882011756.56
# 301   => 
# 1000  => 

def getResult(value):
    global monkeys
    monkeys["humn"].shout = value
    return monkeys["root"].getvalue()

def clearVisitedFlags():
    global monkeys
    for monkeyname in monkeys:
        monkeys[monkeyname].visited = False

def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2

        print(f"searching between {low} and {high} (midpoint {mid}) ")
        print(f"searching between {items[low]} and {items[high]} (midpoint {items[mid]})")


        if search(items[mid]) == target:
            return mid
        elif search(items[mid]) > target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def search(x):
    print(f"***** TESTING {x} ****")
    data()
    for monkeyname in monkeys:
        #print(f"Monkey {monkeyname} is {monkeys[monkeyname]}")
        monkeys[monkeyname].connect()

    monkeys["root"].operation = "="

    clearVisitedFlags()
    monkeys["humn"].shout = x

    diff = monkeys["root"].getvalue()
    print(f"DIFF IS: {diff}")

    return diff


import matplotlib.pyplot as plt
import pandas as pd

def main():
    global monkeys

    #print(search(3373767893067))
    
    #guesses = range(3373767890000,3373767899999)
    guesses = range(0,4373767899999)
    print(binary_search(guesses, 0))

    

    # arr = []
    # for i in range(int(3373767893067*0.99),int(3373767893067*1.01),1000000000):
    #     arr.append(search(i))

    # df = pd.DataFrame(arr)
    # df.plot()
    # plt.show()





if __name__ == "__main__":
    main()
