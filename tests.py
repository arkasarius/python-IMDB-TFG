import xml.etree.ElementTree as ET
import os
import json
import functions as fun
tree = ET.parse('The_Matrix.xml')
root = tree.getroot()
# f = open("test.txt","w+")
# for face in root.iter('Face'):
#     f.write(json.dumps(face.attrib))
# f.close()
a=0
# f = open("ids.txt","w+")
for face in root.iter('Face'):
    # if(a==0):
        # los atributos aun siendo listas son devueltas como caracteres, por lo que se tiene que extraer los caracteres especiales [ ] , por espacios 
        # se tiene que reconvertir a una lista con split.
        # 128 descriptores
        # tensorflow gpu no vol instalarse
        # print(face.attrib)
        # id = int(face.attrib.get('id'))
        # if(id>a):
        #     a=id
        # n=face.attrib.get('face_embedding').replace("[","").replace(",","").replace("]","")
        # n=n.split()
        # print(n[128-1])
        # f.write(id)
    name=int(face.attrib.get('person_id'))
    # print(face.attrib)
    f=open("thematrix/"+str(name)+".txt","a+")
    n=face.attrib.get('face_embedding').replace("[","").replace(",","").replace("]","")
    f.write(n+'\n')
    f.close()
# f.close()
# print(a)

# print(fun.getmAxId(root))