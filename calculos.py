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

folder="moviesdata"
s='/'
root = os.listdir(folder)
for movie in root:
    print(movie)
    actors=os.listdir(folder+s+movie)
    # print(actors)
    for element in actors:
        a=folder+s+movie+s+element
        # print(a)
        b=extraerSublistaArchivo(a)
        # print(b[0])
        # actores=os.listdir("actordata")
        # for elem in actores:
            nombre=elem.strip(".txt")
            # print(nombre)
            # datax=extraerSublistaArchivo("actordata"+s+elem)
            for x in b:
                for y in datax:
                    if distanciaEuclidea(x,y) < 0.6:
                    # print("distanciaEuclidea")
                    # print(distanciaEuclidea(x,y))
                    # print("Similitud coseno")
                    # print(similitudCoseno(x,y))
                        print(nombre+" pertenece al actor de "+a)
        # c=extraerSublistaArchivo("actordata/Bruce Willis.txt")
        # for x in b:
        #     for y in c:
        #         if distanciaEuclidea(x,y) < 0.5:
        #             # print("distanciaEuclidea")
        #             # print(distanciaEuclidea(x,y))
        #             # print("Similitud coseno")
        #             # print(similitudCoseno(x,y))
        #             print("true")
        


# x=extraerSublistaArchivo("moviesdata/The matrix/0.txt")
# y=extraerSublistaArchivo("actordata/Keanu Reeves.txt")
# print(x[1])
# print("///")
# print(y[1])
# print("///")
# print("distancia euclidea")
# print(distanciaEuclidea(x[1],y[1]))
# print("Similitud coseno")
# print(similitudCoseno(x[1],y[1]))

# l=[]
# for i in range(128):
#     l.append(i)
# plt.stackplot(l,x[1],y[1])
# plt.show()
# matplotlib tests


