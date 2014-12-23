from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import xlrd

檔案 = xlrd.open_workbook("台華.xls")
表單 = 檔案.sheet_by_name("ok")
總列數 = 表單.nrows - 1
總行數 = 表單.ncols - 1
現在列 = -1
漢字=''
f = open("台華詞典一對一.txt","w") #opens file with name of "test.txt"
while 現在列 < 總列數:
	現在列 += 1
	row = 表單.row(現在列)
	print('第', 現在列, "筆：")
	現在行 = 3
	while 現在行 > 0:
		現在行 -= 1
		# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
		cell型態 = 表單.cell_type(現在列, 現在行)
		cell內容 = 表單.cell_value(現在列, 現在行)
		if(現在行 ==2):
			漢字=cell內容
		else:
			if(cell型態 !=0):
				try:
					音=cell內容
					_分析器 = 拆文分析器()
					結果 = _分析器.產生對齊組(漢字, 音)
					家私=轉物件音家私()
					# 轉臺羅
					轉了結果=家私.轉音(臺灣閩南語羅馬字拼音, 結果)
					譀鏡=物件譀鏡()
					print(結果)
					print('臺羅:',譀鏡.看型(結果),'/',譀鏡.看音(結果))
					print('通用:',譀鏡.看型(轉了結果),'/',譀鏡.看音(轉了結果))
					print(譀鏡.看分詞(轉了結果))
					f.write(譀鏡.看分詞(轉了結果))
					f.write('\n')
				except:
					print('掠過一筆')
	print('===================================================================')
f.close()