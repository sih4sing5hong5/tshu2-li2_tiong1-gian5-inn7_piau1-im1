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
from 處理中研院標音.第一步共外語處理掉 import 第一步共外語處理掉
class 第一步共外語處理掉試驗(unittest.TestCase):
	def setUp(self):
		self.第一步共外語處理掉=第一步共外語處理掉()
	def tearDown(self):
		pass
	def test_換逝(self):
		原來='''<Sync time="3919.18400000001"/>
la0159214 過去 政府 e 國語 政策， gue4_ki4
<Event desc="ki3" type="lexical" extent="previous"/>
 zing4_hu4 e2 gok1_qi1 zing4_cik2
<Sync time="3921.48800000001"/>
la0159215 ga 咱e 台語 講做 是 北京語 e 方言， ga3 lan1_e2 dai3_qi4 gong1_zor4 si
3 bak1_giann2_qi4 e2 hong2_qen5
'''
		結果='''la0159214 過去 政府 e 國語 政策， gue4_ki4 zing4_hu4 e2 gok1_qi1 zing4_cik2
la0159215 ga 咱e 台語 講做 是 北京語 e 方言， ga3 lan1_e2 dai3_qi4 gong1_zor4 si
3 bak1_giann2_qi4 e2 hong2_qen5
'''
		self.assertEqual(self.第一步共外語處理掉.擲掉外語佮空逝(原來), 結果)
	def test_字有中括號(self):
		原來='''<Sync time="4484.28800000001"/>
la0005185 特別 是 學生 囡仔 歇熱 彼zam， dik3_bet3 si3 hak3_sing2 qin1_a4 hior4_
ruah1 hit1_zam3
<Sync time="4486.68800000001"/>
la0005186 會用得 講， e3_iong3_dit1 gong4
<Sync time="4487.66400000001"/>
la0005187 逐日 下晡 四 五點仔 腳兜 [左右]， dak3_rit3 e3_bo1 si4 qo3_diam1_a1 ka2_dau1 zor1_iu2
<Sync time="4490.64000000001"/>
la0005188 阮 攏 會 來 zia- cit-tor， quan1 long1 e3 lai2 zia1 cit1_tor5
<Sync time="4493.07200000001"/>
la0005189 散步， san4_bo2
<Sync time="4493.87200000001"/>
'''
		結果='''la0005185 特別 是 學生 囡仔 歇熱 彼zam， dik3_bet3 si3 hak3_sing2 qin1_a4 hior4_
ruah1 hit1_zam3
la0005186 會用得 講， e3_iong3_dit1 gong4
la0005187 逐日 下晡 四 五點仔 腳兜 [左右]， dak3_rit3 e3_bo1 si4 qo3_diam1_a1 ka2_dau1 zor1_iu2
la0005188 阮 攏 會 來 zia- cit-tor， quan1 long1 e3 lai2 zia1 cit1_tor5
la0005189 散步， san4_bo2
'''
		self.assertEqual(self.第一步共外語處理掉.擲掉外語佮空逝(原來), 結果)
# 	def test_無確定字(self):

	def test_有外文(self):
		原來='''
<Sync time="4617.984"/>
sg0184014 包括寫報告、/bau2-gua4-sia1-bor4-gor3-
<Sync time="4619.296"/>
sg0184015 工程圖面 ｅ打字、/gang2-ding5-do2-vin2, e2-dann1-ri2-
<Sync time="4621.104"/>
sg0184016 寫E-mail、 上網路 查詢各種資料，/sia1[//], zionn3-vang1-lo2, ca2-sun3-gok1-ziong1-zu2-liau2-
<Sync time="4624.368"/>
sg0184017 會使得講 無一天 不用電腦，/e3-sai1-dit1-gong1, vor2-zit3-gang2, vor2-iong3-den3-nau4-
<Sync time="4627.152"/>
sg0184018 當然電腦鍵盤 是最主要的 輸入工具；/dong2-ren5-den3-nau4-gen4-buann5, si3-zue4-zu1-iau3-e2, su2-rip3-gang2-gu2-
<Sync time="4630.736"/>'''
		結果=['<Sync time="4617.984"/>',
			'sg0184014 包括寫報告、/bau2-gua4-sia1-bor4-gor3-',
			'<Sync time="4619.296"/>',
			'sg0184015 工程圖面 ｅ打字、/gang2-ding5-do2-vin2, e2-dann1-ri2-',
			'<Sync time="4621.104"/>',
			'<Sync time="4624.368"/>',
			'sg0184017 會使得講 無一天 不用電腦，/e3-sai1-dit1-gong1, vor2-zit3-gang2, vor2-iong3-den3-nau4-',
			'<Sync time="4627.152"/>',
			'sg0184018 當然電腦鍵盤 是最主要的 輸入工具；/dong2-ren5-den3-nau4-gen4-buann5, si3-zue4-zu1-iau3-e2, su2-rip3-gang2-gu2-',
			'<Sync time="4630.736"/>']
		self.assertEqual(self.第一步共外語處理掉.擲掉外語佮空逝(原來), 結果)