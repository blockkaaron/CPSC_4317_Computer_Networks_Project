import heapq
'''
Group Members: Aaron Block, Chad Brown, Isha Bherani
CPSC 4317 48F
Fall 2024
Group Project - OurGraph
'''


# Our __init__ file for OurGraph class and references to getters / setters for main
class OurGraph:
    def __init__(self):
        self.graph = {}

    def edges(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        previous_nodes = {node: None for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous_nodes

    def least_distance(self, start, end):
        distances, previous_nodes = self.dijkstra(start)
        path, current = [], end
        while current:
            path.append(current)
            current = previous_nodes[current]
        return path[::-1], distances[end]