import re,sys
import difflib
import fileinput
from aptdaemon.logger import ColoredFormatter
from pprint import pprint
from xml.etree import ElementTree as ET

def strip_str(sentance):#去掉標點符號只剩中文
    sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
    sentance= re.sub('[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\─\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]','', sentance).strip()
    return sentance

def cal_differ(str1,str2):
    d=difflib.SequenceMatcher(None, str1, str2).ratio()
    return d

def strip_TRS2arrat(synbal,openfile):
    
    data=list()
    tree = ET.parse(openfile)#打開產生結果來源的TRS檔案
    
    for turn in tree.findall('.//Turn'):
            #print(turn.attrib.get('speaker'))
            for sync in turn.findall('.//Sync'):#///////////////////////sync tag 底下
                pinying=sync.tail
                
                if(pinying.find(synbal)):
                    pinying=pinying.split(synbal)[-1]
                    pinying=strip_str(pinying)
                    pinying=pinying.strip('\n')
                    
                    if(not(pinying.isspace())):
                        data.append(pinying)
                        #print(pinying)
        
    return data

def strip_TRS_org(openfile):
    
    data=list()
    tree = ET.parse(openfile)#打開產生結果來源的TRS檔案
    
    for turn in tree.findall('.//Turn'):
            #print(turn.attrib.get('speaker'))
            for sync in turn.findall('.//Sync'):#///////////////////////sync tag 底下
                pinying = sync.tail
                pinying = pinying.strip()
                pinying = pinying.replace("\n", " ")
                if(not(pinying.isspace())):
                    data.append(pinying)
                    #print(pinying)
        
    return data

if __name__ == '__main__':
    result=list()
    result2=list()
    list_diff1=list()
    list_diff2=list()
    rate=0
    num_word=0
    num_sentance=0
    num_diff_sentance=0
    d = difflib.Differ()
    writefile=open('gau_files/test比對結果.txt',"wt")
    
    file1_org=strip_TRS_org('gau_files/實驗10_Neighbor004.trs')
    file2_org=strip_TRS_org('gau_files/Answer_Neighbor004.trs')
    
    file1=strip_TRS2arrat('/','gau_files/實驗10_Neighbor004.trs')
    file2=strip_TRS2arrat('/','gau_files/Answer_Neighbor004.trs')
 
    print('******************全篇統計在檔案最下方**************************', file=writefile)
    for idx, val in enumerate(file2):
        sentance1 = file1[idx]
        sentance2 = file2[idx]
        diff1=str()
        diff2=str()
        
        
        if(cal_differ(sentance1,sentance2)!=1)and(cal_differ(sentance1,sentance2)!=0):
            if(len(sentance1)==len(sentance2)):
                num_diff_sentance+=1
                print('第',idx,'組', file=writefile)
                #result.append(str('第'+idx+'組'))
                #print(sentance1)
                print('D：音轉字後版本----------',file1_org[idx], file=writefile)
                #print(sentance2)
                print('E：音轉字校正後版本---',file2_org[idx], file=writefile)
                print('該組別匹配正確率: ',cal_differ(sentance1,sentance2), file=writefile)
                anwser= list(d.compare(sentance1, sentance2))
                #print(anwser)
                for x in anwser:
                    if '-' in x :
                        list_diff1.append(x)
                        diff1+=x
                        #print(diff1, file=writefile)
                        
                    if '+' in x:
                        list_diff2.append(x)
                        diff2+=x
                        #print(diff2, file=writefile)
                print(diff1)
                print(diff1, file=writefile)
                result.append(str(diff1))
                print(diff2, file=writefile)
                result.append(str(diff2))
                result2.append(diff1.strip()+'/'+diff2.strip())
                print('========================================', file=writefile)
        if(cal_differ(sentance1,sentance2)!=0):
            num_sentance+=1
            average_len=(len(sentance1)+len(sentance2))/2
            num_word+=average_len
            rate+=cal_differ(sentance1,sentance2)*average_len
            
        
    print('********************************************', file=writefile)
    print('total_sentance=',num_sentance, file=writefile)
    print('num_diff_sentance=',num_diff_sentance, file=writefile)
    print('total_num=',num_word, file=writefile)
    print('total_rate=',rate, file=writefile)
    print('全篇正確率=',rate/num_word, file=writefile)
    print('********************************************', file=writefile)
    
    #print(result2)
    print(list_diff1)
    print(list_diff2)
    
    myset = set(list_diff1)  #myset是另外一個列表，裡面的內容是mylist裡面的無重複 項
    
    for item in myset:
        print("the %d has found %d" ,(item,list_diff1.count(item)))
    
    
    result=result+result2
    result.sort()
    result2.sort()
    writefile.write('%s' % '\n'.join(result2))
    '''
    result2.sort()
    print(result2)
    result=result+result2
    writefile.write('%s' % '\n'.join(result))
    '''
    