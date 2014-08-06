
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
starttime="0"
startspk="null-speaker"
nowspk="null-speaker"
startcont="null-content"
nowcont="null-content"
f = open('part2_trs_test/PTSN_20121116-zy-121126-121210-121216.trs','r',encoding='UTF-8')    
while i<100:
    content=(f.readline())
    spk=GetSpeak(content)
    tim=Gettime(content)
    cont=Getcontent(f,content,cont)
    i=i+1
    if spk !="null-speaker":
        nowspk=spk
    if cont !="null-content":
        nowcont=cont
        print("------"+nowcont)
    if tim !="null-Time":
        if starttime != tim:
            print(startspk+" || "+starttime+" || "+tim+" || "+startcont)
            starttime=tim
            startspk=nowspk
            startcont=nowcont
            
f.close()
