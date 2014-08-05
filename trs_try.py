
def GetSpeak(content):
    speaker=""
    if content.find("speaker")!=(-1):
        for i in range(4):
            speaker=speaker+content[int(content.find("speaker")+9+i)]
    else:
        speaker="null-speaker"
    return speaker		
def Getcontent(file,content):
    if content.find("Sync time=")!=(-1):
        content=file.readline()
    else:
        content="null-content"
    return content

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
f = open('test.trs','r',encoding='UTF-8')    
while (i<3):
    content=(f.readline())
    print(GetSpeak(content))
    print(Gettime(content))
    print(Getcontent(f,content))
    i=i+1
f.close()
