with open('input-6.txt') as f:
    lines = f.readlines()

line = lines[0]

def is_14_diff(chunk):
    db = set()
    if len(chunk) == 14:
        for c in chunk:
            db.add(c)
        return len(db) == 14
    return False

for x in range(len(line)):
    if x+14 <= len(line):
        chunk = line[x:x+14]
        if is_14_diff(chunk):
            print(x, chunk, f" Answer is {x+14}")
            break

# test cases
# print(is_4_diff("abcd"))
# print(is_4_diff(""))
# print(is_4_diff(" "))
# print(is_4_diff("abca"))
