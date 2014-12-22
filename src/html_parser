from html.parser import HTMLParser
  
file = open('vvrs01-20130301 (20130316)-0416.trs','r',encoding='utf-8')
data = file.read().replace('\t',"")
data2 =data.replace('\n',"")
#data.replace("\t", "")
#print(data2)
 
class MyParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        if(tag=="sync"):
            print(attrs)
            
    def handle_data(self, data): 
        if(self.is_cn_char(data[0])):
            """存入字典"""
            print(data)   
        elif(data[0]=="-" or data[0]==" "):
            """直接接上一行"""
            print("1")    
    
    def is_cn_char(self, i): 
        return 0x4e00<=ord(i)<0x9fa6 
 
    def is_cn_or_en(self, i): 
        o = ord(i) 
        return o<128 or 0x4e00<=o<0x9fa6 
         
parser = MyParser(strict=False)
parser.feed(data2)
#data = open("xml_test.trs",'r', encoding='utf-8')
#print(data.readlines())
