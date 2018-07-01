def solution(file_object):
	file_local=open(file_object,"r+")
	inputData=file_local.readlines()
	result=[]
	for inputString in inputData:
		temp=inputString.strip()
		
		if (temp[0] in ('+','-')):
			if any ((c in ('+','-')) for c in temp[1:]):
				continue
		try:
                        temp=int(temp)
			if temp<=1000000000 and temp>=-1000000000 :
                        	result.append(temp)
                except:
                        pass

	return result
if __name__=='__main__':
	file_object='test.txt'
	print solution(file_object)
