import xml.etree.ElementTree as ET
import os
import json
import functions as fun
tree = ET.parse('The_Matrix.xml')
root = tree.getroot()
a=0
for face in root.iter('Face'):
    name=int(face.attrib.get('person_id'))
    f=open("thematrix/"+str(name)+".txt","a+")
    n=face.attrib.get('face_embedding').replace("[","").replace(",","").replace("]","")
    f.write(n+'\n')
    f.close()
