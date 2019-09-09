import calculos as c
import os

movie="Men in black"
m="moviesdata"
g="actordata"
s='/'
apidata=os.listdir(m+s+movie)
actordata=os.listdir(g+s+movie)
print(movie)
print(apidata)
print(actordata)
DM=0.95 # 0.0 distancia minima posible          0.95 valores aptos        
AM=0.4 # 1.0 angle maxim posible                0.4  valores aptos       
calculos=0
for unkownactor in apidata:
    act=c.extraerSublistaArchivo(m+s+movie+s+unkownactor)
    print("\n")
    print('{} subcaras para el actor {}'.format(len(act),unkownactor.strip('.txt')))
    for subactor in actordata:    
        currentactor=c.extraerSublistaArchivo(g+s+movie+s+subactor)
        count=0
        for subcara in act:
            for caratest in currentactor:
                calculos=calculos+1
                if(c.similitudCoseno(caratest,subcara)>AM):
                    if(c.distanciaEuclidea(caratest,subcara)<DM):
                        count=count+1
        if(count>0):
            print('{} Positivo para el cluster {}, {} positivos para coeficientes AM: {} y DM: {}'.format(subactor.strip('.txt'),unkownactor.strip('.txt'),count,AM,DM))
print("\n")
print('{} pares de caras comparados para la pelicula {}'.format(calculos,movie))
