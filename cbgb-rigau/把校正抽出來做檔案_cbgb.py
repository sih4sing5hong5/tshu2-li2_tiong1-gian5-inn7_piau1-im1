import re,sys
import difflib
import fileinput
from aptdaemon.logger import ColoredFormatter

def strip_str(sentance):#去掉標點符號只剩中文
    sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
    sentance= re.sub('[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\─\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]','', sentance).strip()
    return sentance

def cal_differ(str1,str2):
    d=difflib.SequenceMatcher(None, str1, str2).ratio()
    return d

if __name__ == '__main__':
    file1 = open('Trans/Trans03_20121027_Neighbor-20140416-20140731-20140803(高SIR校正).txt', 'r')#此檔案為正確答案的檔案
    writefile=open('高SIR校正TRS.txt', 'wt')#此檔案為正確答案的檔案
    rate=0
    num_word=0
    num_sentance=0
    num_diff_sentance=0
    result = list()
    
    for line1 in file1.readlines():
        line1 = line1.strip()  
        
        if '校正' in line1:                                #只做結果不做原句部份
            num_sentance+=1
            line1 = line1.split('/')[0]
            print(line1)
            writefile.write(line1+'\n')#寫入字典