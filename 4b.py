def data():
    with open('input-4.txt') as f:
        rows = [row.rstrip().split(",") for row in f]
    return rows

def test_data():
    return [
        ['2-4','6-8'],
        ['2-3','4-5'],
        ['5-7','7-9'],
        ['2-8','3-7'],
        ['6-6','4-6'],
        ['2-6','4-8']
    ]

def overlap(r1,r2):
    for i in r1:
        if i in r2:
            return True
    return False

def solve(rows):
    ranges_tmp = [(row[0].split('-'),(row[1].split('-'))) for row in rows]

    count=0

    for r in ranges_tmp:
        r1 = range(int(r[0][0]),int(r[0][1])+1)
        r2 = range(int(r[1][0]),int(r[1][1])+1)

        print("Testing")

        print("List1:",list(r1))
        print("List2:",list(r2))

        if overlap(r1,r2):
            print("Overlap")
            count+=1

    return count

#print(data())
#print(test_data())

print(solve(data()))
#print(solve(test_data()))