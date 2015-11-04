import re,sys
import difflib
import fileinput
from aptdaemon.logger import ColoredFormatter
from pprint import pprint
from xml.etree import ElementTree as ET
from collections import Counter
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡

def sentance去標點符號(sentance):
        #sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
        sentance= re.sub('[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\；\|\{\}\'\:\;\'\…\[\]\.\<\>\/\?\~\、\！\@\#\&\*\%]',' ', sentance).strip()
        sentance=sentance.strip('*')
        sentance=''.join(sentance.split())
        return sentance
    
def sentance轉通用(sentance):
    tools_分析器 = 拆文分析器()
    tools=轉物件音家私()
    display=物件譀鏡()
    object=tools_分析器.建立句物件(sentance)
    result轉音後=tools.轉音(通用拼音音標, object)
    return display.看型(result轉音後)

def strip_str(sentance):#去掉標點符號只剩中文
    sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
    sentance= re.sub('[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\─\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]','', sentance).strip()
    return sentance

def cal_differ(str1,str2):
    d=difflib.SequenceMatcher(None, str1, str2).ratio()
    return d

def strip_TRS(symbal,openfile):
    
    data=list()
    tree = ET.parse(openfile)#打開產生結果來源的TRS檔案
    
    for turn in tree.findall('.//Turn'):
            #print(turn.attrib.get('speaker'))
            for sync in turn.findall('.//Sync'):#///////////////////////sync tag 底下
                sentance=sync.tail
                
                if(sentance.find(symbal))and (not sentance.isspace()):
                    sentance=sentance.strip('\n')
                    sentance=sentance.split(symbal)
                    
                    data.append(sentance)
                    #print(sentance)
        
    return data

def strip_TRS4校正後漢字(symbal,openfile):
    
    data=list()
    tree = ET.parse(openfile)#打開產生結果來源的TRS檔案
    
    for turn in tree.findall('.//Turn'):
            #print(turn.attrib.get('speaker'))
            for sync in turn.findall('.//Sync'):#///////////////////////sync tag 底下
                sentance=sync.tail
                
                if(sentance.find(symbal))and (not sentance.isspace()):
                    sentance=sentance.strip('\n')
                    sentance=sentance.split(symbal)
                    
                    data.append(sentance)
                    print(sentance)
        
    return data


if __name__ == '__main__':
    writefile=open('重新製作校正檔案_NEIGHBOR_004(含本調).txt',"wt")
    file1=strip_TRS('/','../gau_files/4dic_Neighbor004.trs')
    file2=strip_TRS('//','../gau_files/Answer_Neighbor004.trs')
    
    print(file1)
    #print(file2)
    for idx,句_file2 in enumerate(file2):
        
        for idy,句_file1 in enumerate(file1):
            
            if(句_file1[0]==句_file2[0]):
                print(':',句_file2[-1],'/',句_file1[-1],file=writefile)
    