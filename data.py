import os
folder="outs"
root = os.listdir(folder)
out="actordata/"
# print(root)
for movie in root:
    # print(movie)
    actors = os.listdir(folder+'/'+movie)
    # print(actors)
    for actor in actors:
        print(actor)
        outdata=open(out+actor+'.txt',"w+")
        actordata=os.listdir(folder+'/'+movie+'/'+actor)
        # print(actordata)
        for index,data in enumerate(actordata):
            # print(data)
            fActor=open(folder+'/'+movie+'/'+actor+'/'+data, "r")
            # print(index)
            for a,line in enumerate(fActor):
                # print('*'+str(a+1))
                # print(line)
                outdata.write(line)
            fActor.close()
        outdata.close()    