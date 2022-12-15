from collections import defaultdict
import ast

# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

with open('input-13.txt') as f:
    lines = [row.strip() for row in f]

chunks = split(lines, 3)

level = -1

def compareItems(r1,r2):
    global level
    level += 1
    print(f"{level * ' '}",end="")
    print(f"Comparing: {r1} VS {r2}")

    if type(r1) == int and type(r2) == int:
        return 0 if r1 == r2 else 1 if r1 > r2 else -1
    elif type(r1) == list and type(r2) == int:
        return compareItems(r1,[r2])
    elif type(r1) == int and type(r2) == list:
            return compareItems([r1],r2)
    elif type(r1) == list and type(r2) == list:
        
        if r1 == r2:
            print(f"{level*' '} LISTS ARE EQUAL!")
            return 0
        
        for ix1 in range(max(len(r1),len(r2))):
            if ix1 > len(r1)-1:
                print(f"{level*' '} Ran out of list in R1!")
                return -1
            else:
                if ix1 > len(r2)-1:
                    print(f"{level*' '} Ran out of list in R2!")
                    return 1
                else:
                    comp = compareItems(r1[ix1],r2[ix1])
                    if comp != 0:
                        return comp


        return 0


def expand(r1):
    if type(r1) == int:
        return [r1]
    elif type(r1) == list:

        lst = []
        for ix in r1:
            lst += expand(ix)
        return lst
            
def expandList(lst):
    return [expand(x) for x in lst]

def main():
    global chunks
    global level
    index = 1
    index_sum = 0
    for c in list(chunks):

        r1 = ast.literal_eval(c[0])
        r2 = ast.literal_eval(c[1])

        #print(f"Comparing INDEX {index}")
        #print(expandList(r1))
        #print(expandList(r2))

        level = -1
        if compareItems(r1,r2) <= 0:
            print(f"Correct order: {index}: {r1} VS {r2}")
            index_sum += index
        else:
            print(f"Incorrect order: {r1} VS {r2}")
        index += 1

    print(f"index_sum: {index_sum}")
    

if __name__ == "__main__":
    main()
