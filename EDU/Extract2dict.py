import re
inputfile='Trans_Combine002-110519dancor-1(校).trs.txt'#檔案來源(含路徑)
outputfile='../補全漢全羅/新建字典combine003.txt'#輸出作為字典的檔案(含路徑)

if __name__ == '__main__':
    openfile=open(inputfile,"r")
    result = list()  
    for line in openfile.readlines():                          #依次读取每行  
        line = line.strip()                             #去掉每行头尾空白  
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
            continue                                    #是的话，跳过不处理  
        if '原句'  in line:#只做結果不做原句部份
            continue
        line = line.split('：')[1]
        try:
            sentance = line.split('／ ／')[0]
            spell=line.split('/ /')[1]
        except:
            pass
        if ( len(sentance) and len(spell))and '$'in sentance:#有$$才抓出捱做
            sentance=re.sub(r'\（.*\）','',sentance)#拆掉(裏面的字)
            phraseStr=re.findall(r'\$.*\$',sentance)#找出$裏面包含的字$
            #print(phraseStr)
            for i in phraseStr:#在此把$當中的文字拆開,分為必要與不必要部份
                i=i.strip('*')
                i=''.join(i.split())
                words=i.split('$')
                #print(words)
                #print(words[1::2])
            word=words[1::2]
            
            sentance= re.sub("[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\ ；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]", "", sentance).strip()
            spell=re.sub(r'[^a-zA-Z0-9]',' ',spell).strip()
            
            phone=spell.split()#把拼音拆成衣個一個等等和漢字對應
            if(len(sentance)!=len(phone)):#拼音和漢字部份必須數量相等才能繼續做對應
                continue
            #print(str(word))#所需要的部份
            #print(sentance+'|'+spell)
            
            for word_u in word:
                pingin= ''
                try:
                    p=sentance.index(word_u)
                    strW=word_u.replace('', '-')
                    pingin+=str(strW.strip('-')+'｜')#*****注意此標記
                    for i, c in enumerate(word_u):
                        #print(phone[p+i])
                        pingin+=str(phone[p+i]+'-')
                        
                    result.append(pingin.strip('-'))
                except:
                    pingin= ''
                
            #result.append(sentance+"|"+spell)#保存  
    result.sort()#排序结果  
    print(result)
    open(outputfile, 'w').write('%s' % '\n'.join(result))#寫入字典
    openfile.close()#關閉檔案