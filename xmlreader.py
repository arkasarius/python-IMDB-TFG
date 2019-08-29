import xml.etree.ElementTree as ET
import os
tree = ET.parse('Yo_Robot_e.xml')
root = tree.getroot()
print('---')
try:
    for child in root:
        #print(child.tag, child.attrib)
        for e in child:
            #print(e.tag, ":", e.attrib)
            for i in e:
                #print(i.tag, ":", i.attrib)
                for a in i:
                    #print(a.tag, ":", a.attrib)
                    for t in a:
                        #print('* ', t.tag, ":", t.attrib)
                        for u in t:
                            #print('** ', u.tag, ":", u.attrib)
                            for o in u:
                                print('*** ', o.tag, ":", o.attrib)
                                for x in o:
                                    #print('**** ', x.tag, ":", x.attrib)
                                    for y in x:
                                    # print('***** ', y.tag, ":", y.attrib)
                                        for z in y:
                                            print('****** ', z.tag, ":", z.attrib)
                                            print('---')
except:
    print('error jeje')
print ('***')
type(root)