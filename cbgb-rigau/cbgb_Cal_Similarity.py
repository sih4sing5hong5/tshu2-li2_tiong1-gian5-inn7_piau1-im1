import re,sys
import difflib
import fileinput
from aptdaemon.logger import ColoredFormatter
from pprint import pprint

def strip_str(sentance):#去掉標點符號只剩中文
    sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
    sentance= re.sub('[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\─\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]','', sentance).strip()
    return sentance

def cal_differ(str1,str2):
    d=difflib.SequenceMatcher(None, str1, str2).ratio()
    return d

if __name__ == '__main__':
    file1name='Trans/Trans03_Neighbor001(高SIR校正).txt'
    file2name='Trans/Trans_Neighbor002.trs.txt'
    file1 = open(file1name, 'r')#此檔案為正確答案的檔案
    file2 = open(file2name, 'r')#欲比較的檔案
    writefile=open('Trans/比對結果2.txt',"wt")
    
    result=list()
    result2=list()
    result.append(file1name)
    result.append(file2name)
    
    rate=0
    num_word=0
    num_sentance=0
    num_diff_sentance=0
    d = difflib.Differ()
    
    while 1:
        line1 = file1.readline()
        line2 = file2.readline()
        
        
        if '校正' in line1:                                #只做結果不做原句部份
            num_sentance+=1
            line1 = line1.split('：')[1]
            line2 = line2.split('：')[1]
            sentance1 =strip_str(line1.split('/')[0]).strip('*')
            sentance2 =strip_str(line2.split('/')[0]).strip('*')
            pinying1=line1.split('/')[1]
            pinying2=line2.split('/')[1]
            diff1=str()
            diff2=str()
            
            #result.append(sentance1+'/'+sentance2)
            if(cal_differ(sentance1,sentance2)!=1):
                num_diff_sentance+=1
                print(cal_differ(sentance1,sentance2))
                result.append(str(cal_differ(sentance1,sentance2)))
                print('正確：',sentance1,'/',pinying1)
                result.append('正確：'+str(sentance1)+'/'+str(pinying1))
                print('翻譯：',sentance2,'/',pinying2)
                result.append('翻譯：'+str(sentance2)+'/'+str(pinying2))
                anwser= list(d.compare(sentance1, sentance2))
                for x in anwser:
                    if '-' in x :
                        diff_line1=x
                        diff1+=x
                        #print(diff1)
                        
                    if '+' in x:
                        diff_line2=x
                        diff2+=x
                        #print(diff2)
                
                #print(result2)
                #sys.stdout.writelines(anwser)
                print(diff1)
                result.append(str(diff1))
                print(diff2)
                result.append(str(diff2))
                result2.append(diff1.strip()+'/'+diff2.strip())
                print('------------------------------------------------')
                result.append('------------------------------------------------')
            average_len=(len(sentance1)+len(sentance2))/2
            num_word+=average_len
            rate+=cal_differ(sentance1,sentance2)*average_len
        #line1 = line1.split('：')[1]
        if not line1 and not line2:
            break
    print('********************************************')
    result.append('********************************************')
    print('total_sentance=',num_sentance)
    result.append('total_sentance='+str(num_sentance))
    print('num_diff_sentance=',num_diff_sentance)
    result.append('num_diff_sentance='+str(num_diff_sentance))
    print('total_num=',num_word)
    result.append('total_num='+str(num_word))
    print('total_rate=',rate)
    result.append('total_rate='+str(rate))
    print('average rate=',rate/num_word)
    result.append('average rate='+str(rate/num_word))
    print('********************************************')
    result.append('********************************************')
    result2.sort()
    print(result2)
    result=result+result2
    writefile.write('%s' % '\n'.join(result))
    