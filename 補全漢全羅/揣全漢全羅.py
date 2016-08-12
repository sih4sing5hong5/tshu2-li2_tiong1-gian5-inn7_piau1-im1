import gzip
import pickle
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 補全漢全羅.做辭典 import 斷詞語言模型
from 補全漢全羅.做辭典 import 斷字典
from 補全漢全羅.做辭典 import 斷字語言模型
from 補全漢全羅.做辭典 import 斷詞典
from 臺灣言語工具.解析整理.詞物件網仔 import 詞物件網仔
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語言模型.KenLM語言模型 import KenLM語言模型
from 臺灣言語工具.斷詞.語言模型揀集內組 import 語言模型揀集內組
class 揣全漢全羅:
	辭典揣詞 = 拄好長度辭典揣詞()
	揀集內組 = 語言模型揀集內組()
	_篩仔 = 字物件篩仔()
	_網仔 = 詞物件網仔()
	_分析器 = 拆文分析器()
	def __init__(self, 斷詞=True):
		if 斷詞:
			辭典, 模型 = 斷詞典, 斷詞語言模型
		else:
			辭典, 模型 = 斷字典, 斷字語言模型
		with gzip.open(辭典, 'rb') as f:
			self.辭典 = pickle.load(f)
		self.連詞 = KenLM語言模型(模型)
	def 揣(self, 變調句物件):
		接起來句物件=self._分析器.建立句物件('')
		for 詞 in self._網仔.網出詞物件(變調句物件):
			揣詞結果 = self.辭典揣詞.揣詞(self.辭典, 詞)
			揣著句物件 = 揣詞結果[0]
			接起來句物件.內底集.extend(揣著句物件.內底集)
		for 集物件 in 接起來句物件.內底集:
			for 組物件 in 集物件.內底組:
				for 字物件 in self._篩仔.篩出字物件(組物件):
					if '/' in 字物件.型:
						字物件.型, 字物件.音 = 字物件.型.split('/', 1)
		結果 = self.揀集內組.揀(self.連詞, 接起來句物件)
		return 結果[0] 
