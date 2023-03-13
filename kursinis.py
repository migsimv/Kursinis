import numpy as np

def getVertexDegrees(graph):
    a = []
    num_vertices = len(graph)
    for vertex in range(num_vertices):
        a.append(len(graph[vertex]))
    return a

def k_core(dat, k):
    n = len(dat)
    core = dat.copy()
    while True:
        removed = False
        for i in range(n):
            degr = getVertexDegrees(core)
            if degr[i] < k and degr[i] > 0:
                for v in range(n):
                    for s in core[v]:
                        if i == s:
                            core[v].remove(i)
                        else:
                            core[i] = []
                removed = True
        if not removed:
            break
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

def dfs(graph, visited, vertex, component):
    visited[vertex] = True
    component.append(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor, component)

def findConnectedComponents(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    components = []
    for vertex in range(num_vertices):
        if not visited[vertex]:
            component = []
            dfs(graph, visited, vertex, component)
            components.append(component)
    return components

def getResult(graph):
    result = []
    for vertex in range(len(graph)):
        neighbors = " ".join(str(x) for x in (graph[vertex])) 
        res = (vertex, "->", neighbors)
        line = "{} {} {}".format(res[0], res[1], res[2])
        result.append(line)
    return result

def saveToFile(graph):
    with open("output.txt", "w") as file:
        for res in getResult(graph):
            file.write(res + "\n")

        
def main():
    k = 2
    data = readFromFile()
    core = k_core(data, k)    
    saveToFile(core)

if __name__ == '__main__':
    main()

