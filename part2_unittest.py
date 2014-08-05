import unittest
import part2_test as ty

class CalculatorTest(unittest.TestCase):	

	##read file content
	def getfilecontent(self,file):
		f = open(file,'r',encoding='UTF-8')    
		while True:
		    content=(f.readline())
		    if not content:break
		    filecontent=ty.Getcontent(f,content)
		    if filecontent!="null-content":
		    		return filecontent
		    		break
		f.close()
		
	def getfiletime(self,file):
		f = open(file,'r',encoding='UTF-8')    
		while True:
			time=(f.readline())
			if not time:break
			if ty.Gettime(time)!="null-Time":
				return (ty.Gettime(time))
		f.close()
		
	def getfilespk(self,file):
		f = open(file,'r',encoding='UTF-8')    
		while True:
		    spk=(f.readline())
		    if (ty.GetSpeak(spk)) !="null-speaker":
		    		print(ty.GetSpeak(spk))
		    		return (ty.GetSpeak(spk))
		    if not spk:break
		f.close()
	
	
	#input	
	def setUp(self):
		self.speaker="spk9"
		self.starttime="165.166"
		self.talkcontent="梅子呢//mui-zui4梅子le3呢"
		
		self.speaker1="spk1"
		self.starttime1="89.798"
		self.talkcontent1="ding1-gai4-la3-honnh2,li1-u3-gong1-diorh3-gong1-honnh2-"
		
		
		self.speaker2="spk1"
		self.starttime2="175.477"
		self.talkcontent2="ze1-gan1-na1-ve3-su2- 坤元,坤元 -si2-vor3-honnh2, 坤元法師 -le1-gong1-"
		
		
	def test_spk(self):	
		#content 有字的翻譯
		input='part2_unittest_input/input.trs'
		##file's content
		'''<Turn speaker="spk9" startTime="165.166" endTime="166.172">
				<Sync time="165.166"/>
				梅子呢//<ruby><rb>mui-zui4</rb><rt>梅子</rt></ruby> <ruby><rb>le3</rb><rt>呢</rt></ruby>
				</Turn>'''									 
		self.assertEqual(self.getfilespk(input),self.speaker)		
		
	def test_time(self):	
		#content 有字的翻譯
		input='part2_unittest_input/input.trs'
		##file's content
		'''<Turn speaker="spk9" startTime="165.166" endTime="166.172">
			<Sync time="165.166"/>
			梅子呢//<ruby><rb>mui-zui4</rb><rt>梅子</rt></ruby> <ruby><rb>le3</rb><rt>呢</rt></ruby>
			</Turn>'''			
		self.assertEqual(self.getfiletime(input),self.starttime)		
				
		
	def test_content(self):	#content 有字的翻譯
		input='part2_unittest_input/input.trs'
		##file's content
		'''<Turn speaker="spk9" startTime="165.166" endTime="166.172">
				<Sync time="165.166"/>
				梅子呢//<ruby><rb>mui-zui4</rb><rt>梅子</rt></ruby> <ruby><rb>le3</rb><rt>呢</rt></ruby>
				</Turn>'''									 
		self.assertEqual(self.getfilecontent(input),self.talkcontent)						



'''
	#input_1	
	def test_spk1(self):	
		input1='part2_unittest_input/input_1.trs'
		##file's content 
		''''''<Turn speaker="spk1" startTime="89.798" endTime="97.052">
		<Sync time="89.798"/>
		ding1-gai4-la3-honnh2,li1-u3-gong1-diorh3-gong1-honnh2-
		<Sync time="92.017"/>
		li1-si3-piu4-gi4-huan2-neh2-honnh2-
		<Sync time="93.783"/>
		gong1-zit1-le2-kui2,zit3-dionn2-zi2-pior3,li1-dau4-de4-si3-kui2-sann1-mih1-kuan4,e2-zi2-pior3-
		</Turn>''''''				
		self.assertEqual(ty.GetSpeak(input1),self.speaker1)		
		
	def test_starttime1(self):		
		input1='part2_unittest_input/input_1.trs'
		##file's content 
		''''''<Turn speaker="spk1" startTime="89.798" endTime="97.052">
		<Sync time="89.798"/>
		ding1-gai4-la3-honnh2,li1-u3-gong1-diorh3-gong1-honnh2-
		<Sync time="92.017"/>
		li1-si3-piu4-gi4-huan2-neh2-honnh2-
		<Sync time="93.783"/>
		gong1-zit1-le2-kui2,zit3-dionn2-zi2-pior3,li1-dau4-de4-si3-kui2-sann1-mih1-kuan4,e2-zi2-pior3-
		</Turn>''''''
		self.assertEqual(ty.Gettime(input1),self.starttime1)		
		
		
	def test_content1(self):		
		input1='part2_unittest_input/input_1.trs'
		##file's content 
		''''''<Turn speaker="spk1" startTime="89.798" endTime="97.052">
		<Sync time="89.798"/>
		ding1-gai4-la3-honnh2,li1-u3-gong1-diorh3-gong1-honnh2-
		<Sync time="92.017"/>
		li1-si3-piu4-gi4-huan2-neh2-honnh2-
		<Sync time="93.783"/>
		gong1-zit1-le2-kui2,zit3-dionn2-zi2-pior3,li1-dau4-de4-si3-kui2-sann1-mih1-kuan4,e2-zi2-pior3-
		</Turn>''''''
		self.assertEqual(self.getfilecontent(input1),self.talkcontent1)						





	#input_2	
	def test_spk2(self):		
		##漢羅	()
		input2='part2_unittest_input/input_2.trs'
		##file's content
		''''''<Turn speaker="spk1" startTime="0.000000" endTime="1773.844">
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
		</Turn>''''''
		self.assertEqual(ty.GetSpeak(input2),self.speaker2)		
		
	def test_starttime2(self):
		##漢羅	()
		input2='part2_unittest_input/input_2.trs'
		##file's content
		''''''<Turn speaker="spk1" startTime="0.000000" endTime="1773.844">
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
		</Turn>''''''
		self.assertEqual(ty.Gettime(input2),self.starttime2)		
		
	def test_content2(self):		
		##漢羅	()
		input2='part2_unittest_input/input_2.trs'
		##file's content
		''''''<Turn speaker="spk1" startTime="0.000000" endTime="1773.844">
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
		</Turn>''''''
		self.assertEqual(self.getfilecontent(input2),self.talkcontent2)						

'''
if __name__ == '__main__':
		unittest.main()		