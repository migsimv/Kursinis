import random
import bipartite_graph
import main
import numpy as np
import matplotlib.pyplot as plt
#TODO paziuret del seed
def example():
    #TODO patikrinti arrays nes kazkas negerai
    xArray = generateArr(4, 3.5) 
    yArray = generateArr(4,60)
    bipartite = bipartite_graph.random_bipartite_graph( xArray,yArray, 0.01)
    actorGraph = main.findConnectedActors(len(xArray),bipartite)#TODO histograma
    core = main.getCore(actorGraph,2) #TODO histograma virsuniu laipsniu
    # for key, value in core.items():
        # print(key, ': ', value)
    # components = main.findConnectedComponents(core) #kazkas negerai
    # print("Komponenciu skaicius: ", (len(components)))
    # print("Komponenciu ilgiai: ")
    # for component in components:
        # print(len(component))
    # printHistogram(xArray)
    # printHistogram(yArray)

def printHistogram(arr):
    intervals = []
    for i in range(0, 100, 10):
        intervals.append(i)

    intervals.append(100 - 1)
    fig = plt.figure(figsize =(10, 7))
    print(len(arr))

    plt.hist(arr, intervals)
    
    plt.xlabel('Viršūnės svoris')
    plt.ylabel('Viršūnių skaičius')
    
    plt.show()

def generateArr(A, a):
    array_length = 1000
    xArray = []
 
    for x in range(0, array_length):
        u = random.uniform(0.1, 1)
        bbz = round(pow(u, -a))
        if (bbz >= A):
            xArray.append(bbz)
        else:
            xArray.append(A)
    return xArray
