def test_data():
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",             # Group 1, item type r
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",       # Group 2, item type Z
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

def finder3(src:str, trg1:str, trg2:str):
    for x in src:
        if x in trg1 and x in trg2:
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
    n=3

    chunks = [lines[i:i + n] for i in range(0, len(lines), n)]
    #print(chunks)

    #for ch in chunks:
    #    print(finder3(ch[0],ch[1],ch[2]))

    priorities = [getPriority(finder3(row[0],row[1],row[2])) for row in chunks]

    print(sum(priorities))


solve(data())
solve(test_data())
