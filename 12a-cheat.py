import sys

#FILENAME = sys.argv[1]
FILENAME = "input-12.txt"

# Build a dict with a tuple(x,y) that points to the character at that position
I = { (x,y): c for y, line in enumerate(open(FILENAME).readlines()) 
               for x, c in enumerate(line.strip()) }

# Return a list of tuples that are adjacent to the given tuple
def adjacents(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

# Return True if the move from xy to nxy is possible
def is_possible_move(xy, nxy):
    # If the next position is not in the dict, it's not possible
    # If the next position is an E, it's possible if the difference between the two is 1 or less
    # If the next position is an S, it's possible if the difference between the two is 1 or less
    return ord(I[nxy].replace("E", 'z')) - ord(I[xy].replace("S", "a")) <= 1 if nxy in I else False

# Return a list of tuples that are adjacent to the given tuple and are possible moves
def possible_adjecents(xy):
    return (nxy for nxy in adjacents(xy) if is_possible_move(xy, nxy))

# Recursive function to flood the distance dict with the distance from the start
def flood(dist, layers):
    # Get the last layer of the layers list
    edge = set(nxy for xy in layers[-1] 
                   for nxy in possible_adjecents(xy) if nxy not in dist)
    # Update the distance dict with the distance from the start
    dist.update({ xy: len(layers) for xy in edge })
    # If there are still possible moves, call flood again with the new layer
    if edge:    
        flood(dist, layers + [edge])

# Return the distance from the start to the end
def distance(start, end):
    # Initialize the distance dict with the start position
    dist = { start: 0 }
    # Call flood to fill the distance dict
    flood(dist, [{start}])
    # Return the distance from the start to the end
    return dist[end] if end in dist else 9999

# Return a generator of tuples that have the given value
def find_all(values):
    return (xy for (xy, v) in I.items() if v in values)

# Return the first tuple that has the given value
def find(value):
    return next(find_all(value))

# Print the solution
print("1:", distance(find("S"), find("E")))

# ???
print("2:", min(distance(start, find("E")) for start in find_all(['a', 'S'])))

# find all tuples that have a value of 'a' or 'S'
# for start in find_all(['a', 'S']):
#    print(start)
