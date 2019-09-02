from scipy.spatial import distance
from matplotlib import pyplot as plt
import os

def distanciaEuclidea(a,b):
    return distance.euclidean(a, b)

def similitudCoseno(a,b):
    return 1-distance.cosine(a,b)

def extraerSublistaArchivo (archivo):
    """
    devuelve una lista de listas de descriptores faciales desde una ruta en base float
    """
    a=[]
    f = open(archivo, "r")
    for x in f:
        if x == "":
            break
        x=x.rstrip('\n')
        n=list(x.split(" "))
        for i in range(0, len(n)): 
            n[i] = float(n[i])
        a.append(n)
    f.close()
    return a