def getmAxId(root):
    """Returns the highest id number from the xml """
    a=0
    for face in root.iter('Face'):
        id = int(face.attrib.get('id'))
        if(id>a):
         a=id
    return(a)
def getAttributeList(face):
    n=face.attrib.get('face_embedding').replace("[","").replace(",","").replace("]","")
    n=n.split()
    return n
def getFaceId(face):
    return int(face.attrib.get('id'))