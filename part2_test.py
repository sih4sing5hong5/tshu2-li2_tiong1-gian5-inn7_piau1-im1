
def GetSpeak(content):
    speaker=""
    if content.find("speaker=")!=(-1):
        for i in range(4):
            speaker=speaker+content[int(content.find("speaker=")+9+i)]
    else:
        speaker="null-speaker"
    return speaker		
def Getcontent(file,content,cont):
    if content.find("Sync time=")!=(-1):
        content=file.readline()
    elif content.find("Event desc=") != (-1):
        content=file.readline()
        content=cont+content
    else:
        content="null-content"
    return content.replace("\n"," ")

def Gettime(content):
    Time=""
    i=0
    if content.find("Sync time=")!=(-1):
        while (1):
            if content[((content.find("Sync time=\""))+11+i)]== "\"":
                break;
            else :
                Time=Time+content[((content.find("Sync time=\""))+11+i)]
                i=i+1
    else:
        Time="null-Time"
    return Time

i=0
cont=" "
f = open('part2_trs_test/PTSN_20121116-zy-121126-121210-121216.trs','r',encoding='UTF-8')    
while True:
    content=(f.readline())
    spk=GetSpeak(content)
    tim=Gettime(content)
    cont=Getcontent(f,content,cont)
    if spk !="null-speaker":
        print(spk)
    if tim !="null-Time":
        print(tim)
    if cont !="null-content":
        print(cont)
    if not content:break
f.close()
