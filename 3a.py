def test_data():
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

def data():
    with open('input-3.txt') as f:
        lines = f.readlines()
    return lines

def finder(src:str, trg:str):
    for x in src:
        if x in trg:
            return x
    raise "No char found!"

def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def getPriority(c):
    if c in range_char('a','z'):
        return ord(c)-ord('a')+1
    if c in range_char('A','Z'):
        return ord(c)-ord('A')+27
    raise Exception(f"Invalid char {c}!")
    
    

def solve(lines):
    rows = [ (row[:int(len(row)/2)],row[int(len(row)/2):]) for row in lines]
    #print(rows)
    for row in rows:
        priorities = [getPriority(finder(row[0],row[1])) for row in rows]
    print(sum(priorities))


solve(test_data())
solve(data())
