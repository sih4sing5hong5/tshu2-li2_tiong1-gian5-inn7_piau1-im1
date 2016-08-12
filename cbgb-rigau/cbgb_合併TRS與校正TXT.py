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
    file1 = open('高SIR校正TRS.txt', 'r')#此檔案為正確答案的檔案
    file2 = open('校正後拼音.txt', 'r')#欲比較的檔案
    writefile=open('完整校正檔案.txt',"wt")#寫入結果檔案
    rate=0
    num_word=0
    num_sentance=0
    num_diff_sentance=0
    result = list()
    
    while 1:
        line1 = file1.readline().strip()
        line2 = file2.readline().strip()
        sentance=line1+'/'+line2
        print(sentance)
        writefile.write(sentance+'\n')
        
        if not line1 and not line2:
            break