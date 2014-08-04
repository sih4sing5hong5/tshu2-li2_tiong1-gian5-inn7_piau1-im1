import xml.etree.ElementTree as ET
dict={}
tree = ET.parse('xml_test.trs')
root = tree.getroot()
for Epi in root.findall('Episode'):
    for Sec in Epi.findall('Section'):
        for Turn in Sec.findall('Turn'):
            attribute = Turn.items()
            if(len(attribute)==2):
                dict.update({attribute[0][0] : attribute[0][1]})
                dict.update({attribute[1][0] : attribute[1][1]})
                print("start:",dict['startTime'],"end:",dict['endTime'])
            elif(len(attribute)==3):
                dict.update({attribute[0][0] : attribute[0][1]})
                dict.update({attribute[1][0] : attribute[1][1]})
                dict.update({attribute[2][0] : attribute[2][1]})
                print("start:",dict['startTime'],"end:",dict['endTime'],"speaker:",dict['speaker'])