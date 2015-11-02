# coding=utf-8
from xml.etree import ElementTree as ET
import os,re
from xml.dom import minidom
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
class TRS加漢羅:
    
    def file加漢羅(self,path,openfile,result檔案):
        
        tree = ET.parse(path+openfile)#打開產生結果來源的TRS檔案
        
        for turn in tree.findall('.//Turn'):
            #print(turn.attrib.get('speaker'))
            for sync in turn.findall('.//Sync'):#///////////////////////sync tag 底下
                _openresult=open(path+result檔案,'rt')
                pinying原始=sync.tail
                pinying=sync.tail
                pinying=TRS加漢羅.sentance去標點符號(self,TRS加漢羅.sentance轉台羅(self,pinying))
                for line in _openresult.readlines():
                    if '結果：' in line:   
                        line = line.strip()
                        line = line.split("結果： ")[-1]
                        sentance結果漢羅=line.split("/")[0]
                        sentance結果漢羅=sentance結果漢羅.split("結果：")[-1]
                        sentance結果拼音=line.split("/")[1]
                        sentance原句拼音=line.split("/")[-1]
                        sentance去標點符號的原句拼音=TRS加漢羅.sentance去標點符號(self,sentance原句拼音)
                        if 'xxx7' in sentance去標點符號的原句拼音:
                            list_去標點符號的原句拼音=sentance去標點符號的原句拼音.split('xxx7')
                            list_去標點符號的結果漢羅=sentance結果漢羅.split('xxx7')
                            for idx,pinying_list_原句 in enumerate(list_去標點符號的原句拼音):
                                if pinying_list_原句 == pinying :
                                    sync.tail=pinying原始+'/'+list_去標點符號的結果漢羅[idx]
                        else:
                            if sentance去標點符號的原句拼音 == pinying:
                                sync.tail=pinying原始+'/'+sentance結果漢羅#將原本的句換成整理後的
                #as///////////////////////////////////////////////
            for event in turn.findall('.//Event'):#///////////////////////Event tag 底下
                _openresult=open(path+result檔案,'rt')
                pinying原始=event.tail
                pinying=event.tail
                pinying=TRS加漢羅.sentance去標點符號(self,TRS加漢羅.sentance轉台羅(self,pinying))
                for line in _openresult.readlines():
                    if '結果：' in line:   
                        line = line.strip()
                        line = line.split("結果： ")[-1]
                        sentance結果漢羅=line.split("/")[0]
                        sentance結果漢羅=sentance結果漢羅.split("結果：")[-1]
                        sentance結果拼音=line.split("/")[1]
                        sentance原句拼音=line.split("/")[-1]
                        sentance去標點符號的原句拼音=TRS加漢羅.sentance去標點符號(self,sentance原句拼音)
                        if 'xxx7' in sentance去標點符號的原句拼音:
                            list_去標點符號的原句拼音=sentance去標點符號的原句拼音.split('xxx7')
                            list_去標點符號的結果漢羅=sentance結果漢羅.split('xxx7')
                            for idx,pinying_list_原句 in enumerate(list_去標點符號的原句拼音):
                                if pinying_list_原句 == pinying:
                                    event.tail=pinying原始+'/'+list_去標點符號的結果漢羅[idx]
                        else:
                            if sentance去標點符號的原句拼音 == pinying:
                                event.tail=pinying原始+'/'+sentance結果漢羅#將原本的句換成整理後的
        #write to .trs file below///////////////////////////////////////////////
        #write to .trs file below///////////////////////////////////////////////
        tree.write(path+'實驗_'+openfile,encoding="UTF-8",xml_declaration=True)#寫回TRS檔
        return tree
    
    def sentance去標點符號(self,sentance):
        #sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
        sentance= re.sub('[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]',' ', sentance).strip()
        sentance=sentance.strip('*')
        sentance=''.join(sentance.split())
        return sentance
    
    def sentance轉台羅(self,sentance):
        tools_分析器 = 拆文分析器()
        tools=轉物件音家私()
        display=物件譀鏡()
        object=tools_分析器.建立句物件(sentance)
        result轉音後=tools.轉音(通用拼音音標, object)
        return display.看型(result轉音後)
'''
if __name__ == '__main__':
    dosometing=TRS加漢羅()
    do=dosometing.file加漢羅('../test_yuliau/','PTSN_20121005-zy-121021.trs','Trans_PTSN_20121005-zy-121021.trs.txt')
    '''