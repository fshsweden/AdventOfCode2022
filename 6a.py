with open('input-6.txt') as f:
    lines = f.readlines()

line = lines[0]

def is_4_diff(chunk):
    db = set()
    if len(chunk) == 4:
        db.add(chunk[0])
        db.add(chunk[1])
        db.add(chunk[2])
        db.add(chunk[3])

        return len(db) == 4
    return False

for x in range(len(line)):
    if x+4 <= len(line):
        chunk = line[x:x+4]
        if is_4_diff(chunk):
            print(x, chunk, f" Answer is {x+4}")
            break

# test cases
# print(is_4_diff("abcd"))
# print(is_4_diff(""))
# print(is_4_diff(" "))
# print(is_4_diff("abca"))
