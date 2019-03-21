
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

    

    def depth_first_recursive(self, start):
        visited = {}
        result = []
        def dfs(vertex):
            visited[vertex] = True
            result.append(vertex)
            neighbours = self.adjacency_list[vertex]
            for node in neighbours:
                if node not in visited:
                    dfs(node)
        dfs(start)
        return result

    def depth_first_iterative(self, start):
        visited = {}
        stack = [start]
        result = []
        while stack:
            vertex = stack.pop()
            visited[vertex] = True
            result.append(vertex)
            neighbours = self.adjacency_list[vertex]
            for item in neighbours:
                if item not in stack and item not in visited:
                    stack.append(item)
        return result

    def breadth_first_iterative(self, node):
        visited = {}
        queue = [node]
        result = []
        while queue:
            vertex = queue.pop(0)
            visited[vertex] = True
            result.append(vertex)
            neighbours = self.adjacency_list[vertex]
            for item in neighbours:
                if item not in queue and item not in visited:
                    queue.append(item)
        return result


graph1 = Graph()
graph1.add_vertex("A")
graph1.add_vertex("B")
graph1.add_vertex("C") 
graph1.add_vertex("D")
graph1.add_vertex("E")
graph1.add_vertex("F")
graph1.add_edge("A", "B")
graph1.add_edge("A", "C")
graph1.add_edge("B", "D")
graph1.add_edge("C", "E")
graph1.add_edge("D", "E")
graph1.add_edge("D", "F")
graph1.add_edge("E", "F")
print(graph1.adjacency_list)
print("==========================")
print(graph1.depth_first_recursive("A"))
print("==========================  iterative dfs")
print(graph1.depth_first_iterative("A"))
print("===================== iterative bfs")
print(graph1.breadth_first_iterative("A"))