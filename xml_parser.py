from xml.dom import minidom
from xml.dom.minidom import Node
#file = open("data.txt", 'w')
def remove_blanks(node):
    for x in node.childNodes:
        if x.nodeType == Node.TEXT_NODE:
            if x.nodeValue:
                x.nodeValue = x.nodeValue.strip()
        elif x.nodeType == Node.ELEMENT_NODE:
            remove_blanks(x)
          
def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

xml = minidom.parse('xml_test.trs')
remove_blanks(xml)
xml.normalize()
Turn=xml.getElementsByTagName('Turn')
print(xml.getAttribute('startTime'))
"""with file('file.xml', 'w') as result:
    result.write(xml.toprettyxml(indent = '  '))"""