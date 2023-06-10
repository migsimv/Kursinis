import random
import bipartite_graph
import main
import numpy as np
import matplotlib.pyplot as plt

def example():
    xArray = generateArr(4, 3.5) 
    yArray = generateArr(4,10)
    bipartite = bipartite_graph.random_bipartite_graph(xArray,yArray, 0.005)
    degreesArray = []
    actorGraph = main.findConnectedActors(len(xArray),bipartite)

    for key, value in actorGraph.items():
        # print(key, ': ',(value))
        degreesArray.append(len(value))
    # printHistogram(degreesArray)
    core = main.getCore(actorGraph,1) 
    coreDegreesArray = []
    for key, value in core.items():
        # print(key, ': ', value)
        coreDegreesArray.append(len(value))
    # printHistogram(coreDegreesArray)

    components = main.find_components(core) 
    print("Komponenciu skaicius: ", len(components))
    print("Komponenciu ilgiai: ")
    for component in components:
        print(len(component))
    # printHistogram(xArray)
    # # print(len(yArray))
    # printHistogram(yArray)

def printHistogram(arr):
    intervals = []
    for i in range(0, 1000, 100):
        intervals.append(i)
    intervals.append(1000 - 1)
    x = np.arange(0, 1000, 100)
    y = np.arange(0, 5000, 200)

    plt.xticks(x)
    plt.yticks(y)

    counts, edges, bars = plt.hist(arr, intervals,edgecolor='k')
    plt.bar_label(bars)
    plt.xlabel('Viršūnės svoris')
    plt.ylabel('Viršūnių skaičius')
    
    plt.show()

def generateArr(A, a):
    array_length = 1000
    xArray = []
    random.seed(22)
    for x in range(0, array_length):
        while True:
            u = round(pow(random.uniform(0.1, 1), -a))
            if (u >= A and u <= 1000):
                xArray.append(u)
                break
            if(u <= 1000):
                xArray.append(A)
                break
    return xArray
