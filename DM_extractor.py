import calculos as cc
import os
import matplotlib.pyplot as plt
import numpy as np

actores=[
'actordata/Men in black/Linda Fiorentino.txt',
'actordata/Men in black/Rip Torn.txt',
'actordata/Men in black/Tommy Lee Jones.txt',
'actordata/Men in black/Vincent D\'Onofrio.txt',
'actordata/Men in black/Will Smith.txt',
'actordata/Angeles y demonios/Ayelet Zurer.txt',
'actordata/Angeles y demonios/Ewan McGregor.txt',
'actordata/Angeles y demonios/Pierfrancesco Favino.txt',
'actordata/Angeles y demonios/Stellan Skarsgard.txt',
'actordata/Angeles y demonios/Tom Hanks.txt'
]
clusters=[
'moviesdata/Men in black/03.txt',
'moviesdata/Men in black/05.txt',
'moviesdata/Men in black/02.txt',
'moviesdata/Men in black/04.txt',
'moviesdata/Men in black/00.txt',
'moviesdata/Angeles y demonios/02.txt',
'moviesdata/Angeles y demonios/03.txt',
'moviesdata/Angeles y demonios/05.txt',
'moviesdata/Angeles y demonios/04.txt',
'moviesdata/Angeles y demonios/01.txt'
]
# 
x=[]
y=[]
def calc(j):
    DM=0
    k=[]
    while DM<=2:
        DM=DM+0.01  
        count=0
        for elemento in actor:
            for cara in cluster:
                if(cc.distanciaEuclidea(cara,elemento)<DM):
                    count=count+1
        if(count>0):
            print('{} true per {}, {} vegades DMb DM: {}'.format(clusters[j],actores[j],count,DM))
            k.append(count)
        else:
            k.append(0)
    return k
# 
actor=cc.extraerSublistaArchivo(actores[0])
cluster=cc.extraerSublistaArchivo(clusters[0])
DM=0
print("0")
while DM<=2:
    DM=DM+0.01  
    count=0
    for elemento in actor:
        for cara in cluster:
            if(cc.distanciaEuclidea(cara,elemento)<DM):
                count=count+1
    if(count>0):
        print('{} true per {}, {} vegades DMb DM: {}'.format(clusters[0],actores[0],count,DM))
        x.append(DM)
        y.append(count)
    else:
        x.append(DM)
        y.append(0)

# 
actor=cc.extraerSublistaArchivo(actores[1])
cluster=cc.extraerSublistaArchivo(clusters[1])
z=calc(1) #1 plot
print("1")
actor=cc.extraerSublistaArchivo(actores[2])
cluster=cc.extraerSublistaArchivo(clusters[2])
a=calc(2) #2 plot
print("2")
actor=cc.extraerSublistaArchivo(actores[3])
cluster=cc.extraerSublistaArchivo(clusters[3])
b=calc(3) #3 plot
print("3")
actor=cc.extraerSublistaArchivo(actores[4])
cluster=cc.extraerSublistaArchivo(clusters[4])
c=calc(4) #4 plot
print("4")
actor=cc.extraerSublistaArchivo(actores[5])
cluster=cc.extraerSublistaArchivo(clusters[5])
d=calc(5) #1 plot
print("5")
actor=cc.extraerSublistaArchivo(actores[6])
cluster=cc.extraerSublistaArchivo(clusters[6])
e=calc(6) #2 plot
print("6")
actor=cc.extraerSublistaArchivo(actores[7])
cluster=cc.extraerSublistaArchivo(clusters[7])
f=calc(7) #3 plot
print("7")
actor=cc.extraerSublistaArchivo(actores[8])
cluster=cc.extraerSublistaArchivo(clusters[8])
g=calc(8) #4 plot
print("8")
actor=cc.extraerSublistaArchivo(actores[9])
cluster=cc.extraerSublistaArchivo(clusters[9])
h=calc(9) #4 plot
print("9")





plt.plot(x,y,label="Linda Fiorentino")
plt.plot(x,z,label="Rip Torn")
plt.plot(x,a,label="Tommy Lee Jones")
plt.plot(x,b,label="Vincent D'Onofrio")
plt.plot(x,c,label="Will Smith")
plt.plot(x,d,label="Ayelet Zurer")
plt.plot(x,e,label="Ewan McGregor")
plt.plot(x,f,label="Pierfrancesco Favino")
plt.plot(x,g,label="Stellan Skarsgard")
plt.plot(x,h,label="Tom Hanks")

plt.xlabel("Coeficiente DM")
plt.ylabel("Verdaderos positivos")
plt.grid()
plt.legend()
plt.show()
