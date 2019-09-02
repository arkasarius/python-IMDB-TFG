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
for unkownactor in apidata:
    act=c.extraerSublistaArchivo(m+s+movie+s+unkownactor)
    print("\n")
    print('{} subcaras para el actor {}'.format(len(act),unkownactor.strip('.txt')))
    for subactor in actordata:    
        currentactor=c.extraerSublistaArchivo(g+s+movie+s+subactor)
        count=0
        for subcara in act:
            for caratest in currentactor:
                if(c.similitudCoseno(caratest,subcara)>0.6):
                    if(c.distanciaEuclidea(caratest,subcara)<1):
                        count=count+1
        if(count>0):
            print('{} true per {}, {} vegades'.format(subactor.strip('.txt'),unkownactor.strip('.txt'),count))