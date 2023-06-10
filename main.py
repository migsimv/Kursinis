import example
import numpy as np

def findConnectedActors(x, graph): 
    neighbors = {}
    new_graph = {}

    for i in range(x):
        for neighbor in graph[i]:
            neighbors.setdefault(neighbor, []).append(i)
    for i in range(x):
        new_graph[i] = list({n for neighbor in graph[i] for n in neighbors.get(neighbor, {}) if n != i})

    return new_graph

def getEdgesCount(graph):
    count = 0
    for edges in graph.values():
        count += len(edges)
    return count // 2 

def getVertexDegrees(graph):
    count = []
    num_vertices = len(graph)
    for vertex in range(num_vertices):
        count.append(len(graph[vertex]))
    return count

def getCore(graph, k):
    core = graph.copy()
    degrees = getVertexDegrees(core)
    removed = True
    while removed:
        removed = False
        for i in range(len(graph)):
            if i == 999:
                print(degrees[i])
            if degrees[i] < k and degrees[i] > 0:
                for neighbor in core[i]:
                    core[neighbor].remove(i)
                    degrees[neighbor] -= 1
                core.pop(i)
                degrees[i] = 0
                removed = True
            elif degrees[i] == 0 and core.get(i) is not None:
                core.pop(i)
                removed = True
    return core

def createAdjMatrix(dat): # will not be used in future
    V = len(dat)
    adj_matrix = np.array([[0 for _ in range(V)] for _ in range(V)])
    for node, neighbors in dat.items():
        for neighbor in neighbors:
            adj_matrix[node][neighbor] = 1
    return adj_matrix

def printAdjMatrix(adj_matrix):  # will not be used in future
    print("  ",*range(len(adj_matrix))) 
    i = 0
    for row in adj_matrix:
        print(i,row)
        i += 1

def readFromFile():
    with open('input.txt', 'r') as file:
        file_contents = file.readlines()
    graph = {}
    for line in file_contents:
        parts = line.split('->')
        node = int(parts[0])
        neighbors = list(map(int, parts[1].split()))
        graph[node] = neighbors
    return graph
def find_components(graph):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components

def getResult(graph):
    result = []
    for key, value in graph.items():
        res = (key, "->", value)
        line = "{} {} {}".format(res[0], res[1], res[2])
        result.append(line)
    return result

def saveToFile(graph):
    with open("output.txt", "w") as file:
        for res in getResult(graph):
            file.write(res + "\n")

def componentsSize(components):
    size = []
    for component in components:
        size.append(len(component))
    return size

def main():
    example.example()

if __name__ == '__main__':
    main()

