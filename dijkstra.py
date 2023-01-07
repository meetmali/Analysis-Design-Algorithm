import heapq


class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.min_distance = float('inf')
        self.adjacency_list = []

    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue

            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.end_vertex
                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(self.heap, v)

            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):
        print("Shortest path to vertex is: %s" % str(vertex.min_distance))
        actual_vertex = vertex
        while actual_vertex is not None:
            print("%s " % actual_vertex.name)
            actual_vertex = actual_vertex.predecessor


if __name__ == "__main__":
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(7, node2, node3)
    edge3 = Edge(4, node1, node3)

    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge2)

    algorithm = Dijkstra()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node3)
