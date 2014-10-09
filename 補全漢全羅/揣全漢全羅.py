from 補全漢全羅.做辭典 import tian2
import gzip
import pickle
from 臺灣言語工具.表單.肯語句連詞 import 肯語句連詞
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
語言模型檔 = '例句.lm'
class 揣全漢全羅:
	辭典揣詞 = 拄好長度辭典揣詞()
	揀集內組 = 連詞揀集內組()
	_篩仔 = 字物件篩仔()
	def __init__(self):
		with gzip.open(tian2, 'rb') as f:
			self.辭典 = pickle.load(f)
		self.連詞 = 肯語句連詞(語言模型檔)
	def 揣(self, 變調句物件):
		揣著句物件 = self.辭典揣詞.揣詞(self.辭典, 變調句物件)
		for 集物件 in 揣著句物件.內底集:
			for 組物件 in 集物件.內底組:
				for 字物件 in self._篩仔.篩出字物件(組物件):
					字物件.型, 字物件.音 = 字物件.型.split('/', 1)
		結果 = self.揀集內組.揀(self.連詞, 揣著句物件)
		return 結果[0] 
