import gzip
import pickle
from 臺灣言語工具.表單.肯語句連詞 import 肯語句連詞
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.斷詞.連詞揀集內組 import 連詞揀集內組
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 補全漢全羅.做辭典 import 斷詞語言模型
from 補全漢全羅.做辭典 import 斷字典
from 補全漢全羅.做辭典 import 斷字語言模型
from 補全漢全羅.做辭典 import 斷詞典
class 揣全漢全羅:
	辭典揣詞 = 拄好長度辭典揣詞()
	揀集內組 = 連詞揀集內組()
	_篩仔 = 字物件篩仔()
	def __init__(self, 斷詞=True):
		if 斷詞:
			辭典, 模型 = 斷詞典, 斷詞語言模型
		else:
			辭典, 模型 = 斷字典, 斷字語言模型
		with gzip.open(辭典, 'rb') as f:
			self.辭典 = pickle.load(f)
		self.連詞 = 肯語句連詞(模型)
	def 揣(self, 變調句物件):
		揣詞結果 = self.辭典揣詞.揣詞(self.辭典, 變調句物件)
		揣著句物件 = 揣詞結果[0]
		for 集物件 in 揣著句物件.內底集:
			for 組物件 in 集物件.內底組:
				for 字物件 in self._篩仔.篩出字物件(組物件):
					if '/' in 字物件.型:
						字物件.型, 字物件.音 = 字物件.型.split('/', 1)
		結果 = self.揀集內組.揀(self.連詞, 揣著句物件)
		return 結果[0] 
