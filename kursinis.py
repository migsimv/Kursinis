import numpy as np

def k_core(adj_matrix, k):
    n = adj_matrix.shape[0]
    degrees = np.sum(adj_matrix, axis=1)
    core = adj_matrix.copy()

    while True:
        removed = False
        for i in range(n):
            degr= np.sum(core, axis=1)[i]
            if degr < k and degr > 0:
                core[i,:] = 0
                core[:,i] = 0
                degrees -= core[i,:]
                removed = True
        if not removed:
            break

    return core

def createAdjMatrix(data):
    V = len(data)
    adj_matrix = np.array([[0 for _ in range(V)] for _ in range(V)])
    for node, neighbors in data.items():
        for neighbor in neighbors:
            adj_matrix[node][neighbor] = 1
    return adj_matrix

def printAdjMatrix(adj_matrix):
    print("  ",*range(len(adj_matrix))) 
    i = 0
    for row in adj_matrix:
        print(i,row)
        i += 1

def readFromFile():
    with open('input.txt', 'r') as file:
        file_contents = file.readlines()
    data = []
    graph = {}
    for line in file_contents:
        parts = line.split(':')
        node = int(parts[0])
        neighbors = list(map(int, parts[1].split()))
        graph[node] = neighbors
        data.append((node, neighbors))
    return graph

def main():
    k = 2
    data = readFromFile()

    # edges = [(0,1),(0,2),(0,3),(1,3),(1,2),(2,4),(2,3),(4,5),(5,6),(3,5)]

    adj_matrix = createAdjMatrix(data)
    core = k_core(adj_matrix, k)
    
    # printAdjMatrix(adj_matrix)
    # printAdjMatrix(core)
    print(np.sum(adj_matrix, axis=1))
    print(np.sum(core, axis=1))

if __name__ == '__main__':
    main()

