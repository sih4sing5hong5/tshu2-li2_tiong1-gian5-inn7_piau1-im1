# coding=utf-8
from xml.etree import ElementTree as ET
import os,re
from xml.dom import minidom
openfile='Finish_Neighbor005(陳草).trs'
tree = ET.parse(openfile)
for turn in tree.findall('.//Turn'):
    #print(turn.attrib.get('speaker'))
    for sync in turn.findall('.//Sync'):
        
        #print(sync.tail.split("//")[-1])
        if ' ah' in sync.tail:
            continue
        if '-ah' in sync.tail:
            continue
        else:
            sync.tail=''
tree.write('ah_'+openfile,encoding="UTF-8",xml_declaration=True)