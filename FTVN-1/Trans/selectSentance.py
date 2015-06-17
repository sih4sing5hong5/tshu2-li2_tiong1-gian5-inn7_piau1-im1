if __name__ == '__main__':
    filename='Trans_090522_B_FTVN.trs.txt'
    file = open(filename, 'r')#此檔案為正確答案的檔案
    writefile=open('ah的句子.txt',"wt")
    
    result=list()
    result.append(filename)
    
    for line in file.readlines():  
        if '-ah' in line:                                #只做結果不做原句部份
            result.append(line)

    writefile.write('%s' % '\n'.join(result))#寫入字典
