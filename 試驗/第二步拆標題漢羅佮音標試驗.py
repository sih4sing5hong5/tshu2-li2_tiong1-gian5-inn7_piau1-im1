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
		self.第二步拆標題漢羅佮音標=第二步拆標題漢羅佮音標()
	def tearDown(self):
		pass
	def test_拆開(self):
		原來='sg0050001 海海 人生 ──美麗 ｅ 容顏 /hai1_hai4 rin2_sing1 vi1_le2 e2 iong2_qan4'
		結果=('sg0050001', '海海 人生 ──美麗 ｅ 容顏 ', 'hai1_hai4 rin2_sing1 vi1_le2 e2 iong2_qan4')
		self.assertEqual(self.第二步拆標題漢羅佮音標.拆開一句(原來), 結果)
	def test_拆開無斜線的(self):
		原來='sg0050002 「認真地 為 臺灣 奉獻著 生命 的 人， rin3_zin2_deh1 ui4 dai3_uan5 hong3_hen4_dior3 senn4_mia2 e2 lang5'
		結果=('sg0050002', '「認真地 為 臺灣 奉獻著 生命 的 人，', 'rin3_zin2_deh1 ui4 dai3_uan5 hong3_hen4_dior3 senn4_mia2 e2 lang5')
		self.assertEqual(self.第二步拆標題漢羅佮音標.拆開一句(原來), 結果)
	def test_拆開無斜線漢字有數字的(self):
		原來='dv0094383 同 註 1。 dong2 zu4 it2'
		結果=('dv0094383', '同 註 1。', 'dong2 zu4 it2')
		self.assertEqual(self.第二步拆標題漢羅佮音標.拆開一句(原來), 結果)
	def test_拆開無斜線有標點的(self):
		原來='dv0380181 炒作， ca1_zork2'
		結果=('dv0380181', '炒作，', 'ca1_zork2')
		self.assertEqual(self.第二步拆標題漢羅佮音標.拆開一句(原來), 結果)
	def test_標點佮音標黏做伙(self):
		原來='dv0177001 睏破 三領 蓆，kuan4-pua4 sann2-nia1 ciorh2'
		結果=('dv0177001', '睏破 三領 蓆，', 'kuan4-pua4 sann2-nia1 ciorh2')
		self.assertEqual(self.第二步拆標題漢羅佮音標.拆開一句(原來), 結果)
	def test_一字句(self):
		原來='ch0038812 有！ u2'
		結果=('ch0038812', '有！', 'u2')
		self.assertEqual(self.第二步拆標題漢羅佮音標.拆開一句(原來), 結果)
