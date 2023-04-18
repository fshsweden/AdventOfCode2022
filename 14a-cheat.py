"""
The guy who did this obviously have done this before..
"""
def place_rocks(data):
    rocks = set()
    for line in data.split("\n"):
        
        points = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]

        print(points)

        for i in range(len(points)-1):
            p1, p2 = points[i], points[i+1]
            
            xr = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
            yr = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)

            rocks.update({(x, y) for x in xr for y in yr})

    return rocks

data = open("input-14.txt").read().strip()
print(data)

rocks = place_rocks(data)

# Find the max y value
max_y = max((y for _, y in rocks))

# Start the sand at the origin
x, y = (500, 0)

# Count the number of times the sand hits something
ct = p1 = p2 = 0

while True:

    # If the current point is a rock or a rested sand unit, restart the sand at the origin
    if (x, y) in rocks:
        (x, y) = (500, 0)

    # Did we fal into the abyss (and it hasnt happened before?)
    if y > max_y and p1 == 0:  # abyss part 1
        p1 = ct

    # Move if possible. First try down, then down/left, then down/right
    if (x, y + 1) not in rocks and y < max_y + 1:  # drop down?
        y += 1    
    elif (x - 1, y + 1) not in rocks and y < max_y + 1:  # drop left-down?
        x -= 1
        y += 1
    elif (x + 1, y + 1) not in rocks and y < max_y + 1:  # drop right-down?
        x += 1
        y += 1
    else:  # Impossible to move. Rest sand unit here!
        ct += 1
        rocks.add((x, y))

    # If we haven't moved from origin, we're done
    if (x, y) == (500, 0):  # filled
        p2 = ct
        break

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")