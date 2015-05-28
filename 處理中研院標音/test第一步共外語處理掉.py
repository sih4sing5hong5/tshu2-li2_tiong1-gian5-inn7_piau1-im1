from curses.ascii import isspace
class 第一步共外語處理掉:
	def 擲掉外語佮空逝(self,句集):
		資料=[]
		頂一逝是標籤=True
		外語的開始或外語tag=False
		有外語=False
		for 句 in 句集.split('\n'):
			句=句.rstrip()
			#print(句)
			if 句=='':
				continue
			elif 'language' in 句 or '[//]' in 句:# or '_' in 句:
				if 'begin' in 句 or 'instantaneous' in 句:
					#資料=資料[:-1]
					外語的開始或外語tag=True
				有外語=True
				頂一逝是標籤=False
			#elif 'type="lexical"' in 句:
				#continue
			elif 句.startswith('<') or 句.startswith('\ufeff'):
				頂一逝是標籤=True
				有外語=False
			else:
				if 有外語:
					頂一逝是標籤=True
					if 外語的開始或外語tag:
						資料[-1]+=str(' xxx7 ')
						外語的開始或外語tag=False
					else:
						資料[-1]+=句
				else:
					if 頂一逝是標籤:
						資料.append(句)
					else:
						資料[-1]+=句
					頂一逝是標籤=False
		#print(資料)
		return 資料
