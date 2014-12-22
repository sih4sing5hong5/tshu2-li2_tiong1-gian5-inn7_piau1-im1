import unittest

class part3:

    def compare_fst_string(self,s1):
        '''測試目標1:把編號切出來
        參數:
        s1 - 原句,例如:dv0146003 若是日頭黃昏ｅ時，/na2-si3-rit3-tau5,hong3-hun1-e2-si5-
        fst_result - 可使用的Output(如果測試都Ok),例如:s1[0,9]
        '''   
        tmp=''
        if(s1[9] == ' '):
        #假設編號長度是固定(9)且編號之後會空一格，若沒有例外可直接return 9
        #可能會導致測試失敗的例子:前面9個字是(英文小寫+數字)且第10個字是空格，但不是編號(可能是長度為9的拼音，又用空格斷句)
        #起頭如果是中文，會有problem，所以增加以下程式碼
            for c in s1 :
                if (c>='a' and c<='z') or (c>='0' and c<='9'):
                    tmp = tmp+c
                else:                 
                    break
        if len(tmp) != 9:
        #例外處理:拼音起頭
            tmp=''
            
        fst_result = s1[0:len(tmp)]
        return fst_result


    def compare_end_string(self,s1):
        '''測試目標2:把拼音切出來
        參數:
        s1 - 原句,例如:dv0146003 若是日頭黃昏ｅ時，/na2-si3-rit3-tau5,hong3-hun1-e2-si5-
        end_result - 可使用的Output(如果測試都Ok)
        ''' 
        tmp=len(s1)
        for i in range(len(s1)-1,-1,-1) :
            if (s1[i] != '/') and (s1[i] != '，')and (s1[i] != '：')and (s1[i] != '、'):
                #and (s1[i] != ' ')
                tmp=i
            else:
                break
        end_result = s1[tmp:len(s1)]
        return end_result

    def compare_mid_string(self,s1):
        '''測試目標3:把漢字切出來
        參數:
        s1 - 原句,例如:dv0146003 若是日頭黃昏ｅ時，/na2-si3-rit3-tau5,hong3-hun1-e2-si5-
        mid_result - 可使用的Output(如果測試都Ok)
        ''' 
        tmp=''
        fstIndx = len(self.compare_fst_string(s1))
        endIndx = len(s1)-len(self.compare_end_string(s1))
        while(True):
            if s1[fstIndx] == ' ':
                fstIndx=fstIndx+1
            elif (s1[endIndx-1] == '/'):
                endIndx=endIndx-1
            else:
                break

        mid_result = s1[fstIndx:endIndx]
        return mid_result


class MyTestCase(unittest.TestCase):
    '''(Test case)'''
    
    def setUp(self):
        '''準備工作(Test fixture):預備資源'''
        self.default_greeting =[]
        
        self.default_greeting.append(u"dv0146003 若是日頭黃昏ｅ時，/na2-si3-rit3-tau5,hong3-hun1-e2-si5-")
        self.default_greeting.append(u"ch0067045 dor感嘆講：dor3-gam1-tan4-gong4-")
        self.default_greeting.append(u"dv0146031 街頭巷尾愛睏ｅ貓仔、")
        self.default_greeting.append(u"她在外面洗衣服//aih2 i2 deh1 qua3-kau4 se1-sann1 la3")
        self.default_greeting.append(u"la0220009 ga-zuah就是鉸紙啦！/ga2-zuah2-dor3-si3-ga2-zua4-lah3-")
        self.default_greeting.append(u"zi2-na1-lang5-honnh2,i2-ziok1-qau2-gun1-lun1-zun3-gun4-la3-")
        self.default_greeting.append(u"long1-si3 zit1-le2-sior1-zia4 e3-gong2-lor5")
        self.default_greeting.append(u"無咧計較遐濟（hiah-tsē）。//vor2-leh1-ge4-gau4-hiah1-ze2-")
        self.default_greeting.append(u"044、046 欖仁樹 //")
        self.default_greeting.append(u"bor1(go1)-le3-dai2-siong1 dng4-ai3 dai2-uan5 dau2-zu1")
        self.default_greeting.append(u"sg0036037 你敢edang感受著？/li4-gam1-e3-dang4-gam1-siu2-diorh3-")
        self.default_greeting.append(u"弟弟乖喔//你一定要好好聽話喔//tiann2-ue2 o2 a2-di2-a4 guai1 o2")
        self.default_greeting.append(u"ch0073023 是ｍ是e-sai-ho我看你ｅ人頭籠仔?/si3-m3-si3-e3-sai1-li1-ho3-qua1-kuann4-li4-e3-lang2-tau2-lang1-a4-")
        #self.default_greeting.append(u"")
        
        
        
    def test_compare_fst_string(self):
        '''測試方法:"切編號" don't work'''
        test_fst_greeting = []
        
        test_fst_greeting.append(u"dv0146003")
        test_fst_greeting.append(u"ch0067045")
        test_fst_greeting.append(u"dv0146031")
        test_fst_greeting.append(u"")
        test_fst_greeting.append(u"la0220009")
        test_fst_greeting.append(u"")
        test_fst_greeting.append(u"")
        test_fst_greeting.append(u"")
        test_fst_greeting.append(u"")
        test_fst_greeting.append(u"")
        test_fst_greeting.append(u"sg0036037")
        test_fst_greeting.append(u"")
        test_fst_greeting.append(u"ch0073023")
        #test_fst_greeting.append(u"")

        
        for i in range(0,len(self.default_greeting)):
            #self.assertTrue(compare_fst_string(self.default_greeting[i], test_fst_greeting[i]))
            self.assertEqual( self.default_greeting[i][0:len(s.compare_fst_string( self.default_greeting[i] ))] , test_fst_greeting[i] )

    def test_compare_end_string(self):
        '''測試方法:"切拼音" don't work'''
        test_end_greeting = []
        
        test_end_greeting.append(u"na2-si3-rit3-tau5,hong3-hun1-e2-si5-")
        test_end_greeting.append(u"dor3-gam1-tan4-gong4-")
        test_end_greeting.append(u"")
        test_end_greeting.append(u"aih2 i2 deh1 qua3-kau4 se1-sann1 la3")
        test_end_greeting.append(u"ga2-zuah2-dor3-si3-ga2-zua4-lah3-")
        test_end_greeting.append(u"zi2-na1-lang5-honnh2,i2-ziok1-qau2-gun1-lun1-zun3-gun4-la3-")
        test_end_greeting.append(u"long1-si3 zit1-le2-sior1-zia4 e3-gong2-lor5")
        test_end_greeting.append(u"vor2-leh1-ge4-gau4-hiah1-ze2-")
        test_end_greeting.append(u"")
        test_end_greeting.append(u"bor1(go1)-le3-dai2-siong1 dng4-ai3 dai2-uan5 dau2-zu1")
        test_end_greeting.append(u"li4-gam1-e3-dang4-gam1-siu2-diorh3-")
        test_end_greeting.append(u"tiann2-ue2 o2 a2-di2-a4 guai1 o2")
        test_end_greeting.append(u"si3-m3-si3-e3-sai1-li1-ho3-qua1-kuann4-li4-e3-lang2-tau2-lang1-a4-")
        #test_end_greeting.append(u"")

        for i in range(0,len(self.default_greeting)):
            #self.assertTrue(compare_end_string(self.default_greeting[i], test_end_greeting[i]))
            self.assertEqual( self.default_greeting[i][len(self.default_greeting[i])-len(s.compare_end_string(self.default_greeting[i])):len(self.default_greeting[i])], test_end_greeting[i])

    def test_compare_mid_string(self):
        '''測試方法"切漢字" don't work'''
        test_mid_greeting = []
        
        test_mid_greeting.append(u"若是日頭黃昏ｅ時，")
        test_mid_greeting.append(u"dor感嘆講：")
        test_mid_greeting.append(u"街頭巷尾愛睏ｅ貓仔、")
        test_mid_greeting.append(u"她在外面洗衣服")
        test_mid_greeting.append(u"ga-zuah就是鉸紙啦！")
        test_mid_greeting.append(u"")
        test_mid_greeting.append(u"")
        test_mid_greeting.append(u"無咧計較遐濟（hiah-tsē）。")
        test_mid_greeting.append(u"044、046 欖仁樹 ")
        test_mid_greeting.append(u"")
        test_mid_greeting.append(u"你敢edang感受著？")
        test_mid_greeting.append(u"弟弟乖喔//你一定要好好聽話喔")
        test_mid_greeting.append(u"是ｍ是e-sai-ho我看你ｅ人頭籠仔?")
        #test_mid_greeting.append(u"")
        #test_mid_greeting.append(u"")
        #test_mid_greeting.append(u"")
        #test_mid_greeting.append(u"")

     
        for i in range(0,len(self.default_greeting)):
            #self.assertTrue(compare_mid_string(self.default_greeting, test_mid_greeting))
            self.assertEqual(s.compare_mid_string(self.default_greeting[i]),test_mid_greeting[i])

if __name__ == '__main__':
    s = part3()

    #unittest.main()
    #unittest 測試沒問題，所以註掉(可打開)

    #範例
    test=u"dv0146003 若是日頭黃昏ｅ時，/na2-si3-rit3-tau5,hong3-hun1-e2-si5-"
    print(test)
    print("")
    print(s.compare_fst_string(test))
    print(s.compare_mid_string(test))
    print(s.compare_end_string(test))

'''    
dv0143001 - first_result
蕃薯花遊愛奧蘭之一，- mid_result
han2-zi2-hue1,iu2-ai4-or4-lan5-zi2-it2- -end_result
'''
