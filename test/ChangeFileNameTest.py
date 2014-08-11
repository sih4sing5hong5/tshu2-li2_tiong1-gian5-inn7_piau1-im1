import unittest
from ChangeFileName import changeaa
		
class ChangeFileNameTest(unittest.TestCase):		 
		def setUp(self):
				pass
		
		def test_change(self):
				a,b =('_Chen Su Nian_20-101017','_Chen Su Nian_20-20101017')
				self.assertEqual(changeaa(a), b)
		def test_change1(self):
				a,b =('_chen tsau_20--991012-1201229-1030111-0215','_Chen Tsau_20-20101012-20131229-20140111-20140215')
				self.assertEqual(changeaa(a), b)
		def test_change2(self):
				a,b =('_Chen Tsau_40-1021119-1208-1225','_Chen Tsau_40-20131119-20131208-20131225')
				self.assertEqual(changeaa(a), b)
		def test_change3(self):
				a,b =('0501-230001-110704-0917','0501-230001-20110704-20110917')
				self.assertEqual(changeaa(a), b)
		def test_change4(self):
				a,b =('0706-230001-0823-111228','0706-230001-20110823-20111228')
				self.assertEqual(changeaa(a), None)
if __name__ == '__main__':
		unittest.main()		