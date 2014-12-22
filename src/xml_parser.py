import xml.etree.ElementTree as ET
dict={}
global index
index = 0
tree = ET.parse('xml_test.trs')
root = tree.getroot()
for Epi in root.findall('Episode'):
    for Sec in Epi.findall('Section'):
        for Turn in Sec.findall('Turn'):
            print(Turn.text.split())
#             attri_spk = Turn.items()
#             if(len(attri_spk)==3):
#                 dict.update({attri_spk[0][0] : attri_spk[0][1]})
#                 dict.update({attri_spk[1][0] : attri_spk[1][1]})
#                 dict.update({attri_spk[2][0] : attri_spk[2][1]})
#                 #print("speaker:",dict['speaker'])
#                 for Sync in Turn.findall('Sync'):
#                     attri_sync = Sync.items();
#                     dict.update({'time[',index,']' : attri_sync[1]})
#                     print(dict['time[0]'])