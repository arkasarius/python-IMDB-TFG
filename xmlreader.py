import xml.etree.ElementTree as ET
tree = ET.parse('Yo_Robot.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
root[0][0].text