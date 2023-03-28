from collections import deque
import random

def isBipartite(adj_list):
    V = len(adj_list)
    color = [-1] * V
    queue = deque()

    for i in range(V):
        if color[i] == -1:
            color[i] = 1
            queue.append(i)
            while queue:
                u = queue.popleft()
                for v in adj_list[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True


def random_bipartite_graph(n1, n2, p): #TODO aprasyti funkcija gauti p
    V = n1 + n2
    adj_list = [[] for i in range(V)]
    for i in range(n1):
        for j in range(n1, V):
            if random.random() < p:
                adj_list[i].append(j)
                adj_list[j].append(i)

    return adj_list

def adj_list_to_adj_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in adj_list[i]:
            adj_matrix[i][j] = 1
            
    return adj_matrix

def main():
    adj_list = random_bipartite_graph(8, 3, 0.5)
    matrix = adj_list_to_adj_matrix(adj_list)
    i = 0
    for adj in adj_list:
        print(i, adj)
        i += 1
    for m in matrix:
        print(m)
    print(isBipartite(adj_list))

if __name__ == '__main__':
    main()
