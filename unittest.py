import unittest
		
		

class Getstring:

    def GetSpeak(self, content):
        return speaker
	def Getstarttime(self,content):
		return starttime
	def Getendtime(self,content):
		return endtime
	def Getcontent(self,content):
		return content

class CalculatorTest(unittest.TestCase):                 
	
    input="<Turn speaker="spk9" startTime="165.166" endTime="166.172">
		  <Sync time="165.166"/>
		  梅子呢//<ruby><rb>mui-zui4</rb><rt>梅子</rt></ruby> <ruby><rb>le3</rb><rt>呢</rt></ruby>
		  </Turn>"

    intput_1="<Turn speaker="spk1" startTime="89.798" endTime="97.052">
	<Sync time="89.798"/>
	ding1-gai4-la3-honnh2,li1-u3-gong1-diorh3-gong1-honnh2-
	<Sync time="92.017"/>
	li1-si3-piu4-gi4-huan2-neh2-honnh2-
	<Sync time="93.783"/>
	gong1-zit1-le2-kui2,zit3-dionn2-zi2-pior3,li1-dau4-de4-si3-kui2-sann1-mih1-kuan4,e2-zi2-pior3-
	</Turn>"

	##漢羅  ()
    input_2="<Turn speaker="spk1" startTime="0.000000" endTime="1773.844">
	....
	<Sync time="175.477"/>
	ze1-gan1-na1-ve3-su2-
	<Event desc="zh" type="language" extent="begin"/>
	坤元,坤元
	<Event desc="zh" type="language" extent="end"/>
	-si2-vor3-honnh2,
	<Event desc="zh" type="language" extent="begin"/>
	坤元法師
	<Event desc="zh" type="language" extent="end"/>
	-le1-gong1-
	<Sync time="179.334"/>
	enn3-ze1-le1-gong1,a2-binn4-a2-zong1-tong4,an1-ne1-gang3-kuan4-honnh2-
	</Turn>"


	#input  
    def setUp(self):
	self.speaker="spk9"
	self.starttime="165.166"
	self.endtime="166.172"
	self.content="梅子呢//mui-zui4梅子le3呢"
		
    def test_spk(self):                   
        str = Getstring()
        self.assertEqual(str.GetSpeak(input),self.speaker)    
		
    def test_starttime(self):                   
        str = Getstring()
        self.assertEqual(str.Getstarttime(input),self.starttime)    
		
    def test_endtime(self):                   
        str = Getstring()
        self.assertEqual(str.Getendtime(input).self.endtime)    
		
    def test_content(self):                   
        str = Getstring()
        self.assertEqual(str.Getcontent(input),self.content)            




	#input_1  
    def setUp(self):
	self.speaker="spk1"
	self.starttime="89.798"
	self.endtime="92.017"
	self.content="ding1-gai4-la3-honnh2,li1-u3-gong1-diorh3-gong1-honnh2-"
		
    def test_spk(self):                   
        str = Getstring()
        self.assertEqual(str.GetSpeak(input_1),self.speaker)    
		
    def test_starttime(self):                   
        str = Getstring()
        self.assertEqual(str.Getstarttime(input_1),self.starttime)    
		
    def test_endtime(self):                   
        str = Getstring()
        self.assertEqual(str.Getendtime(input_1).self.endtime)    
		
    def test_content(self):                   
        str = Getstring()
        self.assertEqual(str.Getcontent(input_1),self.content)            





	#input_2  
    def setUp(self):
	self.speaker="spk1"
	self.starttime="175.477"
	self.endtime="179.334"
	self.content="ze1-gan1-na1-ve3-su2- 坤元,坤元 -si2-vor3-honnh2, 坤元法師 -le1-gong1-"
		
    def test_spk(self):                   
        str = Getstring()
        self.assertEqual(str.GetSpeak(input_2),self.speaker)    
		
    def test_starttime(self):                   
        str = Getstring()
        self.assertEqual(str.Getstarttime(input_2),self.starttime)    
		
    def test_endtime(self):                   
        str = Getstring()
        self.assertEqual(str.Getendtime(input_2).self.endtime)    
		
    def test_content(self):                   
        str = Getstring()
        self.assertEqual(str.Getcontent(input),self.content)            



if __name__ == '__main__':
    unittest.main()    