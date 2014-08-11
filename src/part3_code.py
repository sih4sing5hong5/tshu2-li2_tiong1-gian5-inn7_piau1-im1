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


if __name__ == '__main__':
    s = part3()
    #範例
    test=u"dv0146003 若是日頭黃昏ｅ時，/na2-si3-rit3-tau5,hong3-hun1-e2-si5-"
    print(test)
    print("")
    print(s.compare_fst_string(test))
    print(s.compare_mid_string(test))
    print(s.compare_end_string(test))
    
