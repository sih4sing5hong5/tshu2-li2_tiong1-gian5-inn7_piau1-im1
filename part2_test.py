
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
    return content.replace("\n","")

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
endtime="0"
startspk="null-speaker"
endspk="null-speaker"
nowspk="null-speaker"
startcont="null-content"
nowcont="null-content"
f = open('part2_trs_test/blktc25-zy-20131010-0222-1030226.trs','r',encoding='UTF-8')    
while True:
    content=(f.readline())
    if not content:
        print(startspk+" || "+starttime+" || "+endtime+" || "+startcont)
        print(endspk+" || "+endtime+" || "+"end"+" || "+nowcont)
        break
    spk=GetSpeak(content)
    tim=Gettime(content)
    cont=Getcontent(f,content,cont)
    i=i+1
    if spk !="null-speaker":
        nowspk=spk
    if tim !="null-Time" :
        if starttime != tim:
            if starttime == "0" :
                startspk=nowspk
            if endtime !="0" and endtime.find("0.0")==(-1):
                print(startspk+" || "+starttime+" || "+endtime+" || "+startcont)
            starttime=endtime
            endtime=tim
            startspk=endspk
            endspk=nowspk
            startcont=nowcont
    if cont !="null-content":
        nowcont=cont
            
f.close()
