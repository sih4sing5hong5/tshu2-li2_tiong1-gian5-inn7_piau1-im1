"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import unittest
from 處理中研院標音.第二步拆標題漢羅佮音標 import 第二步拆標題漢羅佮音標

class 第二步拆標題漢羅佮音標試驗(unittest.TestCase):
	def setUp(self):
		self.第二步拆標題漢羅佮音標 = 第二步拆標題漢羅佮音標()
	def tearDown(self):
		self.assertEqual(self.第二步拆標題漢羅佮音標.拆開一句(self.原來), self.結果)
	def test_拆開(self):
		self.原來 = 'sg0050001 海海 人生 ──美麗 ｅ 容顏 /hai1_hai4 rin2_sing1 vi1_le2 e2 iong2_qan4'
		self.結果 = ('sg0050001', '海海 人生 ──美麗 ｅ 容顏', 'hai1_hai4 rin2_sing1 vi1_le2 e2 iong2_qan4')
	def test_拆開無斜線的(self):
		self.原來 = 'sg0050002 「認真地 為 臺灣 奉獻著 生命 的 人， rin3_zin2_deh1 ui4 dai3_uan5 hong3_hen4_dior3 senn4_mia2 e2 lang5'
		self.結果 = ('sg0050002', '「認真地 為 臺灣 奉獻著 生命 的 人，', 'rin3_zin2_deh1 ui4 dai3_uan5 hong3_hen4_dior3 senn4_mia2 e2 lang5')
	def test_拆開無斜線漢字有數字的(self):
		self.原來 = 'dv0094383 同 註 1。 dong2 zu4 it2'
		self.結果 = ('dv0094383', '同 註 1。', 'dong2 zu4 it2')
	def test_拆開無斜線有標點的(self):
		self.原來 = 'dv0380181 炒作， ca1_zork2'
		self.結果 = ('dv0380181', '炒作，', 'ca1_zork2')
	def test_標點佮音標黏做伙(self):
		self.原來 = 'dv0177001 睏破 三領 蓆，kuan4-pua4 sann2-nia1 ciorh2'
		self.結果 = ('dv0177001', '睏破 三領 蓆，', 'kuan4-pua4 sann2-nia1 ciorh2')
	def test_一字句(self):
		self.原來 = 'ch0038812 有！ u2'
		self.結果 = ('ch0038812', '有！', 'u2')
	def test_漢字上尾是音標(self):
		self.原來 = 'dv0284204 真正變做 「中國人」ah，zin2-ziann4-ben4-zor4, diong2-gok1-lang5-a2-'
		self.結果 = ('dv0284204', '真正變做 「中國人」ah，', 'zin2-ziann4-ben4-zor4, diong2-gok1-lang5-a2-')
	def test_有標點有空白括號(self):
		self.原來 = 'sg0116001 環保 ｅ 幸運草 我 所 熟sai- ｅ 淑惠 一直 到 今仔日， huan2-bor4- e3- hing3-un3-cau4, qua1- so1- sik3-sai2- e3, siok1-hui2, it1-di3(dit3)- gau4,gin2-na1-lit1-'
		self.結果 = ('sg0116001',
			'環保 ｅ 幸運草 我 所 熟sai- ｅ 淑惠 一直 到 今仔日，',
			'huan2-bor4- e3- hing3-un3-cau4, qua1- so1- sik3-sai2- e3, siok1-hui2, it1-di3(dit3)- gau4,gin2-na1-lit1-')
	def test_中央有舒線(self):
		self.原來 = "dv0146003 若是日頭黃昏ｅ時，/na2-si3-rit3-tau5,hong3-hun1-e2-si5-"
		self.結果 = ('dv0146003',
			'若是日頭黃昏ｅ時，',
			'na2-si3-rit3-tau5,hong3-hun1-e2-si5-')
	def test_中央上尾是標點(self):
		self.原來 = "ch0067045 dor感嘆講：dor3-gam1-tan4-gong4-"
		self.結果 = ('ch0067045',
			'dor感嘆講：',
			'dor3-gam1-tan4-gong4-')
	def test_中央上尾是標點有舒線一(self):
		self.原來 = "la0220009 ga-zuah就是鉸紙啦！/ga2-zuah2-dor3-si3-ga2-zua4-lah3-"
		self.結果 = ('la0220009',
			'ga-zuah就是鉸紙啦！',
			'ga2-zuah2-dor3-si3-ga2-zua4-lah3-')
		
	def test_中央上尾是標點有舒線二(self):
		self.原來 = "sg0036037 你敢edang感受著？/li4-gam1-e3-dang4-gam1-siu2-diorh3-"
		self.結果 = ('sg0036037',
			'你敢edang感受著？',
			'li4-gam1-e3-dang4-gam1-siu2-diorh3-')
	def test_中央上尾是標點有舒線三(self):
		self.原來 = "ch0073023 是ｍ是e-sai-ho我看你ｅ人頭籠仔?/si3-m3-si3-e3-sai1-li1-ho3-qua1-kuann4-li4-e3-lang2-tau2-lang1-a4-"
		self.結果 = ('ch0073023',
			'是ｍ是e-sai-ho我看你ｅ人頭籠仔?',
			'si3-m3-si3-e3-sai1-li1-ho3-qua1-kuann4-li4-e3-lang2-tau2-lang1-a4-')
	def test_中央上尾有兩舒線一(self):
		self.原來 = "dv0180018 『提倡 環境 保護』、 //te3-ciong4 kuan3-ging4 bor1-ho2"
		self.結果 = ('dv0180018',
			'『提倡 環境 保護』、',
			'te3-ciong4 kuan3-ging4 bor1-ho2')
	def test_中央上尾有兩舒線二(self):
		self.原來 = "ch0087399 zit為少女 原來是一位公主。 //zit1-ui3-siau4-lu4, quan2-lai5-si3-zit3-ui3-gong2-zu4"
		self.結果 = ('ch0087399',
			'zit為少女 原來是一位公主。',
			'zit1-ui3-siau4-lu4, quan2-lai5-si3-zit3-ui3-gong2-zu4')
	def test_全羅有外來語(self):
		self.原來 = "sg0184016 寫E-mail、 上網路 查詢各種資料，/sia1[//], zionn3-vang1-lo2, ca2-sun3-gok1-ziong1-zu2-liau2-"
		self.結果 = ('sg0184016',
			'寫E-mail、 上網路 查詢各種資料，',
			'sia1[//], zionn3-vang1-lo2, ca2-sun3-gok1-ziong1-zu2-liau2-')
		
		
 

# 	def test_無全羅(self):
# 		self.原來 = "她在外面洗衣服//aih2 i2 deh1 qua3-kau4 se1-sann1 la3"
# 		self.原來 = "zi2-na1-lang5-honnh2,i2-ziok1-qau2-gun1-lun1-zun3-gun4-la3-"
# 		self.原來 = "long1-si3 zit1-le2-sior1-zia4 e3-gong2-lor5"
# 		self.原來 = "無咧計較遐濟（hiah-tsē）。//vor2-leh1-ge4-gau4-hiah1-ze2-"
# 		self.原來 = "044、046 欖仁樹 //"
# 		self.原來 = "bor1(go1)-le3-dai2-siong1 dng4-ai3 dai2-uan5 dau2-zu1"
# 		self.原來 = "弟弟乖喔//你一定要好好聽話喔//tiann2-ue2 o2 a2-di2-a4 guai1 o2"