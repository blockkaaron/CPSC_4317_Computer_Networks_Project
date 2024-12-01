from __init__ import OurGraph

'''
Group Members: Aaron Block, Chad Brown, Isha Bherani
CPSC 4317 48F
Fall 2024
Group Project - Main
'''


# we need to call our initialized class to reference the simulated network graph in order for the project to begin
project_network = OurGraph()

# here, we define our edges and distances in regard to the project network as shown in project example
edges = [
    ('A', 'B', 2), ('A', 'D', 5),
    ('B', 'C', 2), ('B', 'E', 1),
    ('C', 'D', 2), ('C', 'F', 3),
    ('E', 'F', 3)
]
for u, v, w in edges:
    project_network.edges(u, v, w)

# we must implement the first requirement for the project by printing our forwarding tables for every node
print("Project Starting Forwarding Tables:")
for node in project_network.graph:
    distances, next_hops = project_network.dijkstra(node)
    print(f"Node ID {node}:")
    for destination in distances:
        if destination != node:
            path, _ = project_network.least_distance(node, destination)
            print(f"  Destination Node ID: {destination}, Next Hop Node ID: {path[1] if len(path) > 1 else '-'}, Metric: {distances[destination]}")

# now we move to our second requirement of the project; with the first packet with A as the source and F as the destination
path, cost = project_network.least_distance('A', 'F')
print(f"Packet P1 from A to F travels through: {path}, Total Cost: {cost}")

# to meet the 3rd requirements for the project, here we break the link between B and C
project_network.graph['B'] = [(v, w) for v, w in project_network.graph['B'] if v != 'C']
project_network.graph['C'] = [(v, w) for v, w in project_network.graph['C'] if v != 'B']

print("Forwarding Tables after Link Failure (B-C):")
for node in project_network.graph:
    distances, next_hops = project_network.dijkstra(node)
    print(f"Node ID {node}:")
    for destination in distances:
        if destination != node:
            path, _ = project_network.least_distance(node, destination)
            print(f"  Destination Node ID: {destination}, Next Hop Node ID: {path[1] if len(path) > 1 else '-'}, Metric: {distances[destination]}")

# for our 4th and final implementation of the project, we show data packet P2 being sent from node A to node F and it's path.
path, cost = project_network.least_distance('A', 'F')
print(f"Packet P2 from A to F travels through: {path}, Total Cost: {cost}")