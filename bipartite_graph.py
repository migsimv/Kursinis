from collections import deque
import random
import math

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

def getP(alpha,x,y,n,m):
    return alpha * (x*y) / math.sqrt(n*m)


def random_bipartite_graph(n1, n2, alpha): 
    V = len(n1) + len(n2)
    adj_list = [[] for i in range(V)]
    for i in range(len(n1)):
        f = 0
        for j in range(len(n1), V):
            p = getP(alpha,n1[i],n2[f],len(n1), len(n2))
            a =  random.random()
            print(p, a)
            if a < p:
                adj_list[i].append(j)
                adj_list[j].append(i)
            f += 1
    return adj_list

def adj_list_to_adj_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in adj_list[i]:
            adj_matrix[i][j] = 1
    return adj_matrix

