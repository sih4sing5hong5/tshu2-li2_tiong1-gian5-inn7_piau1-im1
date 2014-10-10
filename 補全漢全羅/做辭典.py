import gzip
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.表單.型音辭典 import 型音辭典
from 臺灣言語工具.語音合成.閩南語變調 import 閩南語變調
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
import pickle
import os

這馬所在 = os.path.dirname(__file__)
txt = os.path.join(這馬所在, '辭典一對一.txt.gz')
tian2 = os.path.join(這馬所在, '本調變調辭典.pickle.gz')
語言模型 = os.path.join(這馬所在, '例句')

# 「｜" 丈-姆｜tiunn7-m2 」｜" 就｜to7 是｜si7 阮｜guan2 某｜boo2 的｜e5 老-母｜lau7-bu2 。｜.
def 檔案加入辭典(檔案, 辭典):
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
辭典 = 型音辭典(1)
with gzip.open(txt, 'rt') as f:
	檔案加入辭典(f, 辭典)
with open(語言模型, 'rt') as f:
	檔案加入辭典(f, 辭典)
with gzip.open(tian2, 'wb') as f:
	pickle.dump(辭典, f,
			protocol=pickle.HIGHEST_PROTOCOL)
