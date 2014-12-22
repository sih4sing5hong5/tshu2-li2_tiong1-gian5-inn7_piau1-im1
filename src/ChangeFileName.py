
# class ChangeFileName:     
def changeaa(origin):
	
	s=origin.split('-')
	c=""
	for i in range(len(s)-1,-1,-1): 
		if(s[i].isnumeric()==True): 
			if(len(s[i])==6): 
				if(int(s[i])<900000): 
					s[i]=str(int(s[i])+20000000) 
					if(int(s[i])>20150000):
						s[i]=str(int(s[i])-20000000)
					else:
						s[i]=s[i]
				else: 
					s[i]=str(int(s[i])+19110000) 
			if(len(s[i])==7): 
				s[i]=str(int(s[i])+19110000) 
			if(len(s[i])==8): 
				s[i]=s[i] 
			else: 
				s[i]=s[i] 
		else: s[i]=s[i]
			
			
	for i in range(1,len(s),+1): 
		if(s[i].isnumeric()==True): 
			if(len(s[i])==4): 
				h=len(s[i-1]) 
				if(int(s[i])>int(s[i-1][h-4:h])): 
					s[i]=s[i-1][0:4]+s[i] 
					if(int(s[i])>20150000):
						return None
				else: 
					s[i]=str(int(s[i-1][0:4])+1)+s[i]
					if(int(s[i])>20150000):
						return None
				
				
	for i in range(0,len(s),1):
		c=c+"-"+s[i]
	k=len(c)
	origin=c[1:k]
	
	return origin
