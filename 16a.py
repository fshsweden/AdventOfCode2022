from collections import defaultdict


"""
This implementation of Dijkstra's algorithm uses a priority queue (implemented using the heapq module in Python) 
to store the nodes that need to be processed. The priority of each node is determined by its cost, which is 
initialized to the weight of the edge between the start node and the node itself for the first node, and is 
updated as the algorithm progresses. The algorithm loops until the queue is empty, processing each node 
in order of increasing cost.

To use this implementation, you can pass in a dictionary representing the graph, with the keys being the 
nodes and the values being a dictionary of the neighbors of each node and their corresponding weights. 
The start and end nodes should also be specified. The function will return a list containing the 
shortest path from the start node to the end node, as well as the cost of the path.

"""
import heapq

def dijkstra(graph, start, end):
    # create a priority queue to store the nodes that need to be processed
    queue = [(0, start)]
    # create a dictionary to store the cost of reaching each node
    costs = {start: 0}
    # create a dictionary to store the predecessor of each node in the shortest path
    predecessors = {}
    # create a set to track the nodes that have been processed
    processed = set()
 
    # loop until the queue is empty
    while queue:
        # pop the node with the lowest cost from the queue
        cost, current = heapq.heappop(queue)
        # skip the node if it has already been processed
        if current in processed:
            continue
        # mark the node as processed
        processed.add(current)
        # if the current node is the end node, we are done
        if current == end:
            break
        # iterate over the neighbors of the current node
        for neighbor, weight in graph[current].items():
            # calculate the cost of reaching the neighbor through the current node
            new_cost = cost + weight
            # update the cost and predecessor of the neighbor if necessary
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                predecessors[neighbor] = current
                # add the neighbor to the queue with its updated cost
                heapq.heappush(queue, (new_cost, neighbor))
 
    # create an empty path
    path = []
    # set the current node to the end node
    current = end
    # loop until we reach the start node
    while current != start:
        # insert the current node at the beginning of the path
        path.insert(0, current)
        # set the current node to its predecessor
        current = predecessors[current]
    # insert the start node at the beginning of the path
    path.insert(0, start)
 
    return path, costs[end]


# Dijkstra's algorithm
# def dijkstra(graph, start, end):
#     shortest_distance = {}
#     predecessor = {}
#     unseenNodes = graph
#     infinity = 9999999
#     path = []
#     for node in unseenNodes:
#         shortest_distance[node] = infinity
#     shortest_distance[start] = 0

#     while unseenNodes:
#         minNode = None
#         for node in unseenNodes:
#             if minNode is None:
#                 minNode = node
#             elif shortest_distance[node] < shortest_distance[minNode]:
#                 minNode = node

#         for childNode, weight in graph[minNode].items():
#             if weight + shortest_distance[minNode] < shortest_distance[childNode]:
#                 shortest_distance[childNode] = weight + shortest_distance[minNode]
#                 predecessor[childNode] = minNode
#         unseenNodes.pop(minNode)

#     currentNode = end
#     while currentNode != start:
#         try:
#             path.insert(0, currentNode)
#             currentNode = predecessor[currentNode]
#         except KeyError:
#             print('Path not reachable')
#             break
#     path.insert(0, start)
#     if shortest_distance[end] != infinity:
#         print('Shortest distance is ' + str(shortest_distance[end]))
#         print('And the path is ' + str(path))


# Solve Advent of Code day 16 part 1
# https://adventofcode.com/2022/day/16

# The input data is a maze of valves and tunnels.
# The tunnels lead to other valves.
# The valves have a flow rate and can be open or closed.
# The goal is to determine the total pressure of the system after 30 minutes.

# The input data is a list of valves and tunnels.
# Each valve has a name, a flow rate, and a list of valves it leads to.
# Each tunnel has a name, a flow rate, and a list of valves it leads to.

# The solution is to use a recursive function to follow the tunnels and valves.
# The recursive function will have to keep track of the total pressure and the number of valves open.


# Utility function to create dictionary
def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

class Valve:
    def __init__(self, valve, flow_rate, leads_to=None):
        self.valve = valve
        self.flow_rate = flow_rate
        self.leads_to = leads_to

    def __repr__(self):
        return f"Valve({self.valve}, {self.flow_rate}, {self.leads_to})"

def data():
    with open('test-input-16.txt') as f:
        lines = [row.strip() for row in f]
    
    valves = {}
    start_valve = None

    for line in lines:
        part1,part2 = line.split(';')
        valveName = part1.split(' ')[1]
        flowRate=int(part1.split(' ')[4].split('=')[1])

        valve = Valve(valveName, flowRate)
        
        #tunnels lead to valves DD, II, BB
        leads_to = [x.strip() for x in part2[23:].split(",")]
        valve.leads_to = leads_to

        if start_valve is None:
            start_valve = valve

        valves[valveName] = valve

    return valves, start_valve

valves, root = data()

def checkValve(valve):
    global valves
    print(valve)
    for v in valve.leads_to:
        print(v)
        checkValve(valves[v])

def main():
    global valves
    total_pressure = 0
    valves_open = 0
    minutes = 30
    checkValve(root)


if __name__ == "__main__":
    main()
