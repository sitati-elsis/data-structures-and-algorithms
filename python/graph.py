
class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_vertex(self, vertex):
        vertex = Node(vertex)
        if vertex.value not in self.adjacency_list:
            self.adjacency_list[vertex.value] = []
        else:
            print(f"{vertex.value} already exists")

    def add_edge(self,vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1) 
        else:
            print("invalid vertex")

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].pop(self.adjacency_list[vertex1].index(vertex2))
            self.adjacency_list[vertex2].pop(self.adjacency_list[vertex2].index(vertex1))
        else:
            print("invalid vertex")

    def remove_vertex(self, vertex):
        while self.adjacency_list[vertex]:
            print(self.adjacency_list[vertex])
            item = self.adjacency_list[vertex][0]
            self.remove_edge(vertex, item)
            self.adjacency_list[vertex].pop(0)
        del self.adjacency_list[vertex]

    def depth_first_recursive(self, vertex):
        visited = {}
        result = []
        def dfs(node):
            visited[node] = True
            result.append(node)
            neighbours = self.adjacency_list[node]
            print(f"These are neighbours{node}:{visited}: {neighbours}")
            for item in neighbours:
                if item not in visited:
                    dfs(item)
        dfs(vertex)

        return result


    
graph1 = Graph()
graph1.add_vertex("A")
graph1.add_vertex("B")
graph1.add_vertex("C")
graph1.add_vertex("D")
graph1.add_vertex("E")
graph1.add_vertex("F")
graph1.add_vertex("G")
graph1.add_vertex("H")
graph1.add_edge("A", "B")
graph1.add_edge("A", "C")
graph1.add_edge("B", "D")
graph1.add_edge("C", "E")
graph1.add_edge("D", "E")
graph1.add_edge("D", "F")
graph1.add_edge("E", "F")
graph1.add_edge("E", "G")
print(graph1.adjacency_list)
print("==========================")
print(graph1.depth_first_recursive("A"))
