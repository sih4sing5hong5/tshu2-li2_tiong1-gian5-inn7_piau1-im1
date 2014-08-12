import os
import json

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
inputfile="PTSN_20121116-zy-121126-121210-121216.trs"
i=1
cont=" "
starttime="0"
endtime="0"
startspk="null-speaker"
endspk="null-speaker"
nowspk="null-speaker"
startcont="null-content"
nowcont="null-content"
outputfile=""
outputjsonspk=[]
outputjsonstart=[]
outputjsonend=[]
outputjsoncont=[]

curDir=os.path.dirname(__file__)
a=os.path.join(curDir,'part2_trs_test',inputfile)
f = open(a,'r',encoding='UTF-8')    
while True:
    content=(f.readline())
    if not content:
        #print(startspk+" || "+starttime+" || "+endtime+" || "+startcont)
        #print(endspk+" || "+endtime+" || "+"end"+" || "+nowcont)
        outputjsonspk.append(startspk)
        outputjsonstart.append(starttime)
        outputjsonend.append(endtime)
        outputjsoncont.append(startcont)
        i=i+1
        outputfile=outputfile+endspk+" | "+endtime+" || "+"end"+" ||| "+nowcont+"\n"
        outputjsonspk.append(endspk)
        outputjsonstart.append(endtime)
        outputjsonend.append("end")
        outputjsoncont.append(nowcont)
        break
    spk=GetSpeak(content)
    tim=Gettime(content)
    cont=Getcontent(f,content,cont)
    if spk !="null-speaker":
        nowspk=spk
    if tim !="null-Time" :
        if starttime != tim:
            if starttime == "0" :
                startspk=nowspk
            if endtime !="0" and endtime.find("0.0")==(-1):
                #print(startspk+" || "+starttime+" || "+endtime+" || "+startcont)
                outputjsonspk.append(startspk)
                outputjsonstart.append(starttime)
                outputjsonend.append(endtime)
                outputjsoncont.append(startcont)
            starttime=endtime
            endtime=tim
            startspk=endspk
            endspk=nowspk
            startcont=nowcont
    if cont !="null-content":
        nowcont=cont
            
f.close()
#print (outputfile)
aaaa=os.path.join(curDir,'part2_transform_txt',inputfile[0:(len(inputfile)-3):1]+'txt')
f=open(aaaa,'w')
f.write(outputfile)
f.close()
outputjsonfile={'speaker':outputjsonspk,'starttime':outputjsonstart,'endtime':outputjsonend,'content':outputjsoncont}
outputjsonfile2=json.dumps(outputjsonfile)
aaaab=os.path.join(curDir,'part2_transform_txt',inputfile[0:(len(inputfile)-3):1]+'json')
f=open(aaaab,'w')
f.write(outputfile)
f.close()