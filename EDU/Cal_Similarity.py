import re
import difflib

def strip_str(sentance):#去掉標點符號只剩中文
    sentance= re.sub(r'\（.*\）','',sentance)#拆掉(裏面的字)
    sentance= re.sub("[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]", "", sentance).strip()
    return sentance

def cal_differ(str1,str2):
    d=difflib.SequenceMatcher(None, str1, str2).ratio()
    return d

if __name__ == '__main__':
    openfile=open('Trans02_Combine002-110519(dancor)-1.trs.txt',"r")
    rate=0
    num_word=0
    
    for line in openfile.readlines():                   #依次读取每行  
        line = line.strip()                             #去掉每行头尾空白  
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
            continue                                    #是的话，跳过不处理  
        if '原句'  in line:#只做結果不做原句部份
            continue
        line = line.split('：')[1]
        try:
            sentance1 =strip_str(line.split('／ ／')[0]).strip() 
            sentance2 =strip_str((line.split('／ ／')[1]).split('/ /')[0]).strip() 
            if(len(sentance1)==len(sentance2)):
                print('正確：',sentance1,'/翻譯：',sentance2)
                print(cal_differ(sentance1,sentance2))
                average_len=(len(sentance1)+len(sentance2))/2
                num_word+=average_len
                rate+=cal_differ(sentance1,sentance2)*average_len
        except:
            pass
    print('total_num=',num_word)
    print('total_rate=',rate)
    print('rate=',rate/num_word)
    