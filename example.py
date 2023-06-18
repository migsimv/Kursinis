import random
import bipartite_graph
import main
import numpy as np
import matplotlib.pyplot as plt

def example():
    xArray = generateArray(4, 3.5) 
    yArray = generateArray(4,0.2)
    bipartite = bipartite_graph.random_bipartite_graph(xArray,yArray, 0.5)
    degreesArray = []
    nznArray = []
    for value in bipartite:
        nznArray.append(len(value))
    printHistogram(nznArray, 'Dvidalio grafo viršūnių laipsniai')
    actorGraph = main.findConnectedActors(len(xArray),bipartite)
    for key, value in actorGraph.items():
        degreesArray.append(len(value))
    printHistogram(degreesArray, 'Aktorių grafo viršūnių laipsniai')
    core = main.getCore(actorGraph, 150) 
    coreDegreesArray = []
    for key, value in core.items():
        coreDegreesArray.append(len(value))
    printHistogram(coreDegreesArray, 'Šerdies viršūnių laipsniai')
    components = main.find_components(core) 
    print("Komponenciu skaicius: ", len(components))
    print("Komponenciu ilgiai: ")
    for component in components:
        print(len(component))
    printHistogram(xArray, 'Aktorių viršūnių svoriai')
    printHistogram(yArray, 'Atributų viršūnių svoriai')

def printHistogram(arr, subtitle):
    intervals = []
    for i in range(0, 1000, 100):
        intervals.append(i)
    intervals.append(1000 - 1)
    # x = np.arange(0, 1000, 100)
    # y = np.arange(0, 5000, 200)
    x = np.arange(0, 1000, 100)
    y = np.arange(0, 5000, 200)
    plt.xticks(x)
    plt.yticks(y)

    counts, edges, bars = plt.hist(arr, intervals,edgecolor='k')
    plt.bar_label(bars)
    plt.suptitle(subtitle)
    # plt.xlabel('Viršūnės svoris')
    plt.xlabel('Viršūnės laipsnis')

    plt.ylabel('Viršūnių skaičius')
    
    plt.show()

def generateArray(A, a):
    array_length = 1000
    xArray = []
    random.seed(22)
    for x in range(0, array_length):
        while True:
            u = (pow(random.random(), -a))
            if (u >= A and u <= 1000):
                xArray.append(u)
                break
            if(u <= 1000):
                xArray.append(A)
                break
    return xArray
