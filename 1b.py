with open('input-1.txt') as f:
    lines = f.readlines()

# calculate sum of numbers in lines array until blank line found
def sum_numbers(lines):
    sums = []
    sums.append(0)
    index=0
    for line in lines:
        if line == '' or line == '\n':
            sums.append(0)
            index += 1
        else:
            sums[index] += int(line)
    return sums

sums = sum_numbers(lines)
top3 = sorted(sums, reverse=True)[:3]

print(sum(top3))
