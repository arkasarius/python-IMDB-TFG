import calculos as c
import os

import matplotlib.pyplot as plt
import numpy as np

movie="Men in black"
m="moviesdata"
g="actordata"
s='/'
apidata=os.listdir(m+s+movie)
actordata=os.listdir(g+s+movie)
print(movie)
print(apidata)
print(actordata)
DM=2 # 0.0 distancia minima posible
AM=1 # 1.0 angle maxim posible 

x=[]
y=[]
while AM>=0:

    AM=AM-0.01
    # DM=1.2
    x.append(1-AM)

    for unkownactor in apidata:
        act=c.extraerSublistaArchivo(m+s+movie+s+unkownactor)
        # print("\n")
        # print('{} subcaras para el actor {}'.format(len(act),unkownactor.strip('.txt')))
        for subactor in actordata:    
            currentactor=c.extraerSublistaArchivo(g+s+movie+s+subactor)
            count=0
            for subcara in act:
                for caratest in currentactor:
                    if(c.similitudCoseno(caratest,subcara)>AM):
                        if(c.distanciaEuclidea(caratest,subcara)<DM):
                            count=count+1
            if(count>0):
                print('{} true per {}, {} vegades amb AM: {}'.format(subactor.strip('.txt'),unkownactor.strip('.txt'),count,1-AM))
                y.append(count)
            else:
                y.append(0)
            #     pass
            #     print("no hi han cares valides per els coeficients AM : {} i DM: {} per l'actor {}".format(AM,DM,subactor.strip('.txt')))
    # DM=50
# plt.style.use('bmh')

plt.plot(x,y)
plt.title(actordata[0].strip(".txt"))
plt.xlabel("Coeficiente AM")
plt.ylabel("Verdaderos positivos")
plt.grid()
plt.show()
