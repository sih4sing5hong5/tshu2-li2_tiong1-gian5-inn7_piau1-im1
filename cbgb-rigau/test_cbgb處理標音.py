# coding=utf-8
import os
from 處理中研院標音.test第一步共外語處理掉 import 第一步共外語處理掉
from 處理中研院標音.第二步拆標題漢羅佮音標 import 第二步拆標題漢羅佮音標
from 處理中研院標音.第三步整理文本格式 import 第三步整理文本格式
from 處理中研院標音.第四步建立句物件 import 第四步建立句物件
from 處理中研院標音.臆全漢全羅 import 臆全漢全羅
from 處理中研院標音.test新增TRS漢羅 import TRS加漢羅

if __name__ == '__main__':
	共外語處理掉 = 第一步共外語處理掉()
	拆標題漢羅佮音標 = 第二步拆標題漢羅佮音標()
	整理文本格式 = 第三步整理文本格式()
	建立物件 = 第四步建立句物件()
	全漢全羅 = 臆全漢全羅()
	路徑 = "../cbgb-rigau/"
	結果資料夾= "Trans/"
	os.chdir(路徑)
	
	for 檔名 in sorted(os.listdir(".")):
		if 檔名.endswith("Neighbor001.trs"):
			檔案 = open(路徑+檔名)
			全部語料 = 檔案.read()
			檔案.close()
			print('已讀取：',檔名)
			結果檔名= "實驗_"+檔名+".txt"
			結果檔案= open(路徑+結果資料夾 + 結果檔名,"wt")#寫入結果檔案
			
			無外語 = 共外語處理掉.擲掉外語佮空逝(全部語料)
			#print(無外語)
			分堆句 = 拆標題漢羅佮音標.拆開(無外語)
			#print(分堆句)
			整理堆 = 整理文本格式.整理(分堆句)
			#print(整理堆)
			臺羅堆 = 建立物件.建立(整理堆)
			#print(臺羅堆)
			漢羅 = 全漢全羅.建立(臺羅堆)

			for 結果 in 漢羅:
				#print('原句：', 結果[1], '/', 結果[2],)
				#print('結果：', 結果[3], '/', 結果[4], '/', 結果[2],)
				結果檔案.write('結果：'+結果[3]+'/'+結果[4]+'/'+結果[2]+'\n')			
				#print()
			結果檔案.close()
			
			#/////////////////////////////////////////////////////////////////////////////////////////////
			做TRS檔案=TRS加漢羅()
			TRS檔=做TRS檔案.file加漢羅(路徑,檔名,結果資料夾+ 結果檔名)
			print('路徑:',路徑)
			print('檔名:',檔名)
			print('結果檔名:',結果檔名)
			print('=====================翻譯完成=======================')
			#break