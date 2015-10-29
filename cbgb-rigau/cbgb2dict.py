import re
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚

inputfile='完整校正檔案.txt'#檔案來源(含路徑)
outputfile='../補全漢全羅/cbgb字典.txt'#輸出作為字典的檔案(含路徑)

if __name__ == '__main__':
    openfile=open(inputfile,"r")
    result = list()  
    for line in openfile.readlines():                          #依次读取每行  
        line = line.strip()                             #去掉每行头尾空白  
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
            continue                                    #是的话，跳过不处理  
        if '原句'  in line:#只做校正不做原句部份
            continue
        if '結果'  in line:#只做校正不做結果部份
            continue
        line = line.split('：')[1]
        try:
            sentance = line.split('/')[0]
            spell=line.split('/')[1]
        except:
            continue
        if ( len(sentance) and len(spell)):#有$$才抓出捱做
            sentance=re.sub(r'\（.*\）','',sentance)#拆掉(裏面的字)
            sentance= re.sub("[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\ ；\|\{\}\'\:\;\'\,\…\─\[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]", "", sentance).strip()
            print(sentance)
            print(spell)
            try:
                tool分析器=拆文分析器()
                set=tool分析器.產生對齊組(sentance,spell)
                mirror=物件譀鏡()
            except:
                continue
            #print(line)
            #print(mirror.看分詞(set))
            #print('=================================================================================================')
            '''
            for i in phraseStr:#在此把$當中的文字拆開,分為必要與不必要部份
                i=i.strip('*')
                i=''.join(i.split())
                words=i.strip()
                #print(words)
                #print(i)
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
                '''
            result.append(mirror.看分詞(set))#保存  
            
    result.sort()#排序结果  
    #print(result)
    open(outputfile, 'w').write('%s' % '\n'.join(result))#寫入字典
    openfile.close()#關閉檔案