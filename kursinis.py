import numpy as np

def get_vertex_degrees(graph):
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
            degr = get_vertex_degrees(core)
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

def createAdjMatrix(dat): # will not be used in futures
    V = len(dat)
    adj_matrix = np.array([[0 for _ in range(V)] for _ in range(V)])
    for node, neighbors in dat.items():
        for neighbor in neighbors:
            adj_matrix[node][neighbor] = 1
    return adj_matrix

def printAdjMatrix(adj_matrix):  # will not be used in futures
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

def find_connected_components(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    components = []
    for vertex in range(num_vertices):
        if not visited[vertex]:
            component = []
            dfs(graph, visited, vertex, component)
            components.append(component)
    return components


def main():
    k = 2
    data = readFromFile()

    print(get_vertex_degrees(data))
    core = k_core(data, k)    
    print(get_vertex_degrees(core))
    print(find_connected_components(core))

if __name__ == '__main__':
    main()

