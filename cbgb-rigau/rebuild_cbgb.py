# coding=utf-8
from xml.etree import ElementTree as ET
import os,re
from xml.dom import minidom
from builtins import len
from _ast import Str
openfile='20121027_Neighbor-20140416-20140731-20140803-new.trs'
outputfile=open('新的TRS.txt','wt')#寫入結果檔案'新的TRS.txt'#輸出作為字典的檔案(含路徑)
result = list()  

tree = ET.parse(openfile)
for turn in tree.findall('.//Turn'):
    #print(turn.attrib.get('speaker'))
    for sync in turn.findall('.//Sync'):
        
        #print(sync.tail.split("//")[-1])
        pinying=sync.tail
        #print(newPinying)
        if not pinying.isspace():
            print(pinying)
            #result.append(pinying)
            outputfile.write(pinying)#寫入字典
        
        #print(pinyingArray)