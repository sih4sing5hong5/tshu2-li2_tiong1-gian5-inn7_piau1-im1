# coding=utf-8
import os,re
from xml.etree import ElementTree as ET
from 處理中研院標音.第一步共外語處理掉 import 第一步共外語處理掉
from 處理中研院標音.第二步拆標題漢羅佮音標 import 第二步拆標題漢羅佮音標
from 處理中研院標音.第三步整理文本格式 import 第三步整理文本格式
from 處理中研院標音.第四步建立句物件 import 第四步建立句物件
from 處理中研院標音.上尾轉做HTS標仔 import 上尾轉做HTS標仔
from 處理中研院標音.臆全漢全羅 import 臆全漢全羅

def strip_str(sentance):#去掉標點符號只剩中文
	sentance= re.sub(u'\（.*\）','',sentance)#拆掉(裏面的字)
	sentance= re.sub('[A-Za-z0-9\[\『\』\`\~\!\﹐\@\-\#\$\^\&\？\，\*\(\)\。\「\」\=\_\：\；\|\{\}\'\:\;\'\,\… \[\]\.\<\>\/\?\~\、\！\@\#\\\&\*\%]','', sentance).strip()
	sentance=sentance.strip('*')
	sentance=''.join(sentance.split())
	return sentance

def check_len(sentance):
	len1=len(strip_str(sentance.split('/ /')[0]))
	str2=(sentance.split('/ /')[1].replace ('-',' ')).split()
	len2=len(str2)
	if(len1!=len2):
		return '(字數不等)'
	else:
		return ''

if __name__ == '__main__':
	共外語處理掉 = 第一步共外語處理掉()
	拆標題漢羅佮音標 = 第二步拆標題漢羅佮音標()
	整理文本格式 = 第三步整理文本格式()
	建立物件 = 第四步建立句物件()
	轉做HTS標仔 = 上尾轉做HTS標仔()
	全漢全羅 = 臆全漢全羅()
	資料 = "../cbgb-rigau/"
	
	os.chdir(資料)
	這馬目錄 = os.path.dirname(os.path.abspath(__file__))
	合成語料檔名 = os.path.join(這馬目錄, '合成語料')
	合成語料檔案 = open(合成語料檔名, 'w')
	for 檔名 in sorted(os.listdir(".")):
		if 檔名.endswith("20121027_Neighbor-20140416-20140731-20140803.trs"):
			print(檔名)
			檔案 = open(資料 + 檔名)
			全部語料 = 檔案.read()
			檔案.close()
			無外語 = 共外語處理掉.擲掉外語佮空逝(全部語料)
# 			print(無外語[:10])
			分堆句 = 拆標題漢羅佮音標.拆開(無外語)
# 			print(分堆句[:10])
			整理堆 = 整理文本格式.整理(分堆句)
# 			print(整理堆[:10])
			臺羅堆 = 建立物件.建立(整理堆)
# 			print(臺羅堆[:10])
			轉做HTS標仔.建立(臺羅堆)
			漢羅 = 全漢全羅.建立(臺羅堆)
			結果檔案= open(資料 + "Trans/Trans02_"+檔名+".txt","wt")#寫入結果檔案
			for 結果 in 漢羅:
				print('原句：', 結果[1], '/', 結果[2],)
				結果檔案.write('原句：'+結果[1]+'/'+結果[2]+'\n')
				
				#print(check_len(結果[2]),'結果：', 結果[3], '/', 結果[4],)										#有檢字數對齊
				#結果檔案.write(check_len(結果[2])+'結果：'+結果[3]+'/'+結果[4]+'\n\n')	#有檢字數對齊
				print('結果：', 結果[3], '/', 結果[4],)																					#沒有檢字數對齊
				結果檔案.write('結果：'+結果[3]+'/'+結果[4]+'\n\n')													#沒有檢字數對齊
				print()
			break
			'''
			for 原文, 整理, 臺羅 in zip(無外語, 整理堆, 臺羅堆):
				整理編號, 通用漢羅, 通用全羅 = 整理
				臺羅編號, 臺羅漢羅, 臺羅全羅 = 臺羅
				if not 原文.startswith(整理編號) or 整理編號 != 臺羅編號:
					raise RuntimeError('{0}編號無仝'.format(整理編號))
				print(整理編號, 臺羅全羅, file=合成語料檔案)
			print(len(臺羅堆))
			'''
			結果檔案.close()
