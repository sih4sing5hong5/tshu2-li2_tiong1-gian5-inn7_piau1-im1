# coding=utf-8
from xml.etree import ElementTree as ET
import os,re
from xml.dom import minidom
openfile='Combine003.trs'
tree = ET.parse(openfile)
for turn in tree.findall('.//Turn'):
    #print(turn.attrib.get('speaker'))
    for sync in turn.findall('.//Sync'):
        
        #print(sync.tail.split("//")[-1])
        hanruo=sync.tail.split("//")[0]
        pinying=sync.tail.split("//")[-1]
        pinyingArray=re.split(r'[-,]+', pinying)
        newPinyingArray=[]
        for word in pinyingArray:
            m = re.findall(r'\[([^]]*)\]',word)
            if m:
                word=''.join(map(str,m))
                word=re.sub('[+]','', word).strip()
                newPinyingArray.append(word)
                #print(word)
            else:
                newPinyingArray.append(word)
                #print(word)
        newPinying='-'.join(map(str,newPinyingArray))
        #print(newPinying)
        print(hanruo,newPinying)
        #print(pinyingArray)
        sync.tail=hanruo+'//'+newPinying#將原本的句換成整理後的
tree.write('rebuild_'+openfile,encoding="UTF-8",xml_declaration=True)