# main function and creation of graph

def generate_edges(graph):
    edges = []
    for nodes in graph:
        for neighbour in graph[nodes]:
            edges.append((nodes, neighbour))
    return edges


def find_path_two_vertices(graph,start, end, path=[]):
    # adding first node to path
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    # if start and end are different
    for node in graph[start]:
        if node not in path:
            newpath = find_path_two_vertices(graph, node, end, path)
            if newpath:
                return newpath
    return None


def shortest_path_two_vertices(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return start
    shortest_path = None
    for node in graph[start]:
        if node not in path:
            newpath = shortest_path_two_vertices(graph, node, end, path)
            if newpath:
                if not shortest_path or len(shortest_path) < len(newpath):
                    shortest = newpath

    return shortest
if __name__ == "__main__":
    graph = {
        'A': ['A', 'B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'G': [],
        'F': []
    }

    print(graph['A'])
    print ("The nodes/vertices of the graph", graph.keys, "\n The edges of graph: for keys{0}, are {1}".format(graph.keys(), graph.values()))
    print("The generated edges are :", generate_edges(graph))
    print("Path between two vertices:", find_path_two_vertices(graph, 'A', 'D', path=[]))
    print("Shortest path between two vertices", shortest_path_two_vertices(graph, 'A', 'D', path=[]))