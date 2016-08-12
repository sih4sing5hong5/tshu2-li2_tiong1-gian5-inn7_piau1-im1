from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
import re

class EDU做例句:
    Inputfile_path=''   #輸入的來源檔案
    Outputfile_path=''  #作為例句檔案
    def get_context(self,line):
        line_list=list()
        if '原句'  in line:#只做結果不做原句部份
            return ''
        else:
            line = line.split('：')[1]
            try:
                sentance = line.split('／ ／')[0]
                spell=line.split('/ /')[1]
                sentance=self.strip_str(sentance)
                line_list.append(sentance)
                line_list.append(spell)
                return line_list
            except:
                pass
        
    def strip_str(self,sentance):#去掉標點符號只剩中文
        sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
        sentance= re.sub('[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]','', sentance).strip()
        sentance=sentance.strip('*')
        sentance=''.join(sentance.split())
        return sentance
    
    def check_len(self,sentance):#檢查字數 或 限制長度
        len1=len(sentance[0])
        str2=(sentance[1].replace ('-',' ')).split()
        len2=len(str2)
        #print(sentance,'(',len1,len2,')')
        if(len1!=len2):
            return False
        else:
            return True
        
if __name__ == '__main__':
    EDU做例句=EDU做例句()
    EDU做例句.Inputfile_path='Trans004/Trans_Combine010.trs.txt'
    EDU做例句.Outputfile_path='../補全漢全羅/新建例句/新建例句010txt'
    EDU新建例句檔=open(EDU做例句.Outputfile_path,'wt')
    
    openfile=open(EDU做例句.Inputfile_path,"r")
    result = list()
    for line in openfile.readlines():                          #依次读取每行  
        line = line.strip()                             #去掉每行头尾空白  
        #print(line)
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
            continue                                    #是的话，跳过不处理  
        line=EDU做例句.get_context(line)
        try:
            print(EDU做例句.check_len(line))
            if(EDU做例句.check_len(line)):#檢查漢字和拼音字數是否相符可對齊
                #print(line[1])
                EDU漢字=line[0]
                EDU_拼音=line[1]
                EDU_分析器 = 拆文分析器()
                EDU_結果 =EDU_分析器.產生對齊組(EDU漢字, EDU_拼音)
                EDU譀鏡=物件譀鏡()
                print(EDU譀鏡.看分詞(EDU_結果))
                
                EDU新建例句檔.write(EDU譀鏡.看分詞(EDU_結果))
                EDU新建例句檔.write(' 。｜. \n')
        except:
            pass
    EDU新建例句檔.close()