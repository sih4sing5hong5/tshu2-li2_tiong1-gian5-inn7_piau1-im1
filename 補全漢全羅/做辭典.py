import gzip
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.表單.型音辭典 import 型音辭典
from 臺灣言語工具.語音合成.閩南語變調 import 閩南語變調
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import pickle
import os
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔

這馬所在 = os.path.dirname(__file__)
辭典一對一 = os.path.join(這馬所在, '辭典一對一.txt.gz')
斷字典 = os.path.join(這馬所在, '本調變調字典.pickle.gz')
斷詞典 = os.path.join(這馬所在, '本調變調詞典.pickle.gz')
斷字語言語料 = os.path.join(這馬所在, '斷字例句.txt')
斷詞語言語料 = os.path.join(這馬所在, '斷詞例句.txt')
例句總整理=os.path.join(這馬所在, '訓練用斷詞例句總2.txt')

#ngram-count -order 3 -interpolate -wbdiscount -unk -text 斷字例句.txt -lm 斷字例句.lm
#ngram-count -order 3 -interpolate -wbdiscount -text 斷詞例句.txt -text 斷詞新聞句.txt -lm 斷詞例句.lm
#/home/joseyarashio/文件/srilm-1.7.1/bin/i686-m64/ngram-count -order 3 -interpolate -wbdiscount -text 新建例句013.txt -text 斷詞例句.txt -text 05.華臺校對有例句.txt -text 05.典藏校對有例句.txt -lm 斷詞例句.lm
#/home/joseyarashio/文件/srilm-1.7.1/bin/i686-m64/ngram-count -order 3 -interpolate -wbdiscount  -text 斷詞例句.txt -text 05.華臺校對有例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt -text 新建例句.txt  -text 05.典藏校對有例句.txt -lm 斷詞例句3.lm
#/home/joseyarashio/文件/srilm-1.7.1/bin/i686-m64/ngram-count -order 3 -interpolate -wbdiscount -text 訓練用斷詞例句總2.txt -lm 斷詞例句.lm
斷字語言模型 = os.path.join(這馬所在, '斷字例句.lm')
斷詞語言模型 = os.path.join(這馬所在, '斷詞例句.lm')

if __name__ == '__main__':
	# 「｜" 丈-姆｜tiunn7-m2 」｜" 就｜to7 是｜si7 阮｜guan2 某｜boo2 的｜e5 老-母｜lau7-bu2 。｜.
	def 檔案加入字典(檔案, 辭典):
		_分析器 = 拆文分析器()
		_篩仔 = 字物件篩仔()
		_變調 = 閩南語變調()
		for line in f:
	# 		print(line)
			try:
				句物件 = _分析器.轉做句物件(line)
				for 字物件 in _篩仔.篩出字物件(句物件):
					字物件.型 += '/' + 字物件.音
					詞物件 = _分析器.建立詞物件('')
					詞物件.內底字 = [字物件]
					辭典.加詞(詞物件)
					拼音 = 臺灣閩南語羅馬字拼音(字物件.音)
					if 拼音.音標 != None:
						拼音.聲, 拼音.韻, 拼音.調 = _變調.實詞變調(拼音.聲, 拼音.韻, 拼音.調)
						拼音.做音標()
						字物件.音 = 拼音.音標
						辭典.加詞(詞物件)
			except:
				pass
	def 檔案加入辭典(檔案, 辭典):
		def 變調(音):
			拼音 = 臺灣閩南語羅馬字拼音(音)
			if 拼音.音標 != None:
				拼音.聲, 拼音.韻, 拼音.調 = _變調.實詞變調(拼音.聲, 拼音.韻, 拼音.調)
				拼音.做音標()
				return 拼音.音標
			return 音
		_分析器 = 拆文分析器()
		_篩仔 = 字物件篩仔()
		_網仔 = 詞物件網仔()
		_變調 = 閩南語變調()
		for line in f:
			try:
				句物件 = _分析器.轉做句物件(line.strip())
				for 詞物件 in _網仔.網出詞物件(句物件):
					字陣列 = 詞物件.內底字
					for 字物件 in 字陣列[:]:
						字物件.型 += '/' + 字物件.音
					for 所在 in range(len(字陣列)-1):
						字陣列[所在].音=變調(字陣列[所在].音)
					詞物件 = 詞(字陣列)
# 					print(詞物件)
					辭典.加詞(詞物件)
					
					字陣列[-1].音 = 變調(字陣列[-1].音)
					詞物件 = 詞(字陣列)
# 					print(詞物件)
					辭典.加詞(詞物件)
			except:
				pass
			
	def 檔案加入辭典_不變調(檔案, 辭典):
		_分析器 = 拆文分析器()
		_篩仔 = 字物件篩仔()
		_網仔 = 詞物件網仔()
		
		for line in f:
			try:
				句物件 = _分析器.轉做句物件(line.strip())
				for 詞物件 in _網仔.網出詞物件(句物件):
					字陣列 = 詞物件.內底字
					for 字物件 in 字陣列[:]:
						字物件.型 += '/' + 字物件.音
					詞物件 = 詞(字陣列)
# 					print(詞物件)
					辭典.加詞(詞物件)
					
					詞物件 = 詞(字陣列)
# 					print(詞物件)
					辭典.加詞(詞物件)
			except:
				pass
			
# 	字典 = 型音辭典(1)
# 	with gzip.open(辭典一對一, 'rt') as f:
# 		檔案加入字典(f, 字典)
# 	with gzip.open(斷字典, 'wb') as f:
# 		pickle.dump(字典, f,protocol=pickle.HIGHEST_PROTOCOL)
#		--------------------將新的辭典加入在底下------------------------
	辭典 = 型音辭典(4)
	with gzip.open(辭典一對一, 'rt') as f:
		檔案加入辭典(f, 辭典)
	with open(斷詞語言語料, 'rt') as f:
		檔案加入辭典(f, 辭典)
	with open(例句總整理, 'rt') as f:
		檔案加入辭典(f, 辭典)
	with open('05.典藏校對有例句.txt','rt') as f:
		檔案加入辭典(f, 辭典)
	with open('cbgb001字典.txt','rt') as f:
		檔案加入辭典(f, 辭典)
		
	with open('cbgb002字典.txt','rt') as f:
		檔案加入辭典_不變調(f, 辭典)
	with open('cbgb004字典.txt','rt') as f:
		檔案加入辭典_不變調(f, 辭典)
		
	with open('台華詞典一對一.txt','rt') as f:
		檔案加入辭典(f, 辭典)
	with open('05.華臺校對有例句.txt','rt') as f:
		檔案加入辭典(f, 辭典)
	with open('新建字典combine001.txt','rt') as f:
		檔案加入辭典(f, 辭典)
	with open('新建字典combine002.txt','rt') as f:
		檔案加入辭典(f, 辭典)
	with open('附錄句一對一斷詞.txt','rt') as f:
		檔案加入辭典(f, 辭典)
	with open('斷詞新聞句.txt','rt') as f:
		檔案加入辭典(f, 辭典)
	with open('對齊平行閩南語資料', 'rt') as f:
		檔案加入辭典(f, 辭典)
	with gzip.open(斷詞典, 'wb') as f:
		pickle.dump(辭典, f,protocol=pickle.HIGHEST_PROTOCOL)
