import re
import difflib
from collections import Counter
import unicodedata

def strip_str(sentance):#去掉標點符號只剩中文
    sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
    sentance= re.sub('[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]','', sentance).strip()
    return sentance

def cal_differ(str1,str2):
    d=difflib.SequenceMatcher(None, str1, str2, autojunk=True).ratio()
    return d

if __name__ == '__main__':
    
    file目標檔='Trans_Combine004.trs.txt'
    
    
    openfile=open('Trans006/'+file目標檔,'rt')
    writefile=open('比對結果/實驗二結果'+file目標檔+'.txt',"wt")
    print('******************全篇統計在檔案最下方**************************', file=writefile)
    d = difflib.Differ()
    result=list()
    result2=list()
    list_diff1=list()
    list_diff2=list()
    num_sentance=0
    num_diff_sentance=0
    rate=0
    num_word=0
     
    for idx,line in enumerate(openfile.readlines()):                   #依次读取每行  
        diff1=str()
        diff2=str()
            
        line = line.strip()                             #去掉每行头尾空白  
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
            continue                                    #是的话，跳过不处理  
        if '原句'  in line:                                #只做結果不做原句部份
            continue
        line = line.split('：')[1]
        try:
            num_sentance+=1
            
            sentance1 =strip_str(line.split('／ ／')[0]).strip()
            sentance2 =strip_str((line.split('／ ／')[1]).split('/ /')[0]).strip() 
            #sentance1=''.join(sentance1.split())
            #sentance2=''.join(sentance2.split())
            sentance1 = sentance1.replace("\n","")
            sentance2 = sentance2.replace("\n","")
            #sentance1=sentance1.decode('latin-1').encode('utf-8')  
           
            if(len(sentance1)==len(sentance2)):
                
                result.append(sentance1+'/'+sentance2)
                average_len=((len(sentance1)+len(sentance2))/2)
                num_word+=average_len
                rate+=cal_differ(sentance1,sentance2)*average_len
                
                if cal_differ(sentance1,sentance2)!=1:
                    num_diff_sentance+=1
                    anwser= list(d.compare(sentance1, sentance2))
                    for x in anwser:
                        if '-' in x :
                            list_diff1.append(x)
                            diff1+=x
                            #print(diff1, file=writefile)
                        
                        if '+' in x:
                            list_diff2.append(x)
                            diff2+=x
                    
                    print('第',idx,'組', '|正確率：',cal_differ(sentance1,sentance2),file=writefile)
                    print('第',idx,'組', '|正確率：',cal_differ(sentance1,sentance2))
                    print('正確：',sentance1,'\n翻譯：',sentance2, file=writefile)
                    print('正確：',sentance1,'\n翻譯：',sentance2)
                    print(ord(sentance1))
                    print(diff1, file=writefile)
                    print(diff1)
                    result.append(str(diff1))
                    print(diff2, file=writefile)
                    print(diff2)
                    result.append(str(diff2))
                    result2.append(diff1.strip()+'/'+diff2.strip())
                    print('--', file=writefile)
                    print('--')
            
        except:
            pass
        
    print('********************錯譯字整理******************************', file=writefile)
    print('********************錯譯字整理******************************')
    result=result+result2
    result.sort()
    result2.sort()
    print('%s' % '\n'.join(result2), file=writefile)
    print('%s' % '\n'.join(result2))
    print('\n*****************************************************', file=writefile)
    print('\n***********************錯譯字統計************************', file=writefile)
    count=Counter(list_diff2)
    sum_count=sum(Counter(list_diff2).values())
    
    for x in sorted(count):
        print(x,"{:.2%}".format(count[x]/sum_count), file=writefile)
        print(x,"{:.2%}".format(count[x]/sum_count))
    print('Total',sum_count,'in',count, file=writefile)
    print('Total',sum_count,'in',count)
    print('************************全篇統計**************************', file=writefile)
    print('************************全篇統計**************************')
    print('total_sentance=',num_sentance, file=writefile)
    print('total_sentance=',num_sentance)
    print('num_diff_sentance=',num_diff_sentance, file=writefile)
    print('num_diff_sentance=',num_diff_sentance)
    print('total_num=',num_word, file=writefile)
    print('total_num=',num_word)
    print('total_rate=',rate, file=writefile)
    print('total_rate=',rate)
    print('全篇正確率=',round(rate/num_word,3), file=writefile)
    print('全篇正確率=',round(rate/num_word,3))
    #writefile.write('%s' % '\n'.join(result))
    #print (sys.getdefaultencoding())