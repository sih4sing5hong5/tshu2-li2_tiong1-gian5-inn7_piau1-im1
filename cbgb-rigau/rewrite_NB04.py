import re,sys
import difflib
import fileinput
from aptdaemon.logger import ColoredFormatter
from pprint import pprint
from xml.etree import ElementTree as ET
from collections import Counter

if __name__ == '__main__':
    tree = ET.parse('Neighbor004_1113.trs')#打開產生結果來源的TRS檔案
    
    #for turn in tree.findall('.//Turn'):
            #print(turn.attrib.get('speaker'))
    for sync in tree.findall('.//Sync'):#///////////////////////sync tag 底下
        pinying=sync.tail
                
        if(pinying.find('//')):
            pinying=pinying.split('//')[0]
            sync.tail=pinying
            
    tree.write('re_Neighbor004_1113.trs',encoding="UTF-8",xml_declaration=True)#寫回TRS檔