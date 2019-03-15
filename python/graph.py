# implementation of an undirected graph using Adjacency Lists

class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbour(self, vertex):
        if vertex not in self.neighbours:
            self.neighbours.append(vertex)
            self.neighbours.sort()


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            for key, value in self.vertices.items():
                if key = vertex1:
                    value.add_neighbour(vertex2)
                if key = vertex2:
                    value.add_neighbour(vertex1)
            return True
        else:
            return False



