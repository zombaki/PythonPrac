def solution(file_object):
	file_local=open(file_object,"r+")
	inputData=file_local.readlines()
	result_c=[]
	result_cpp=[]
	result_cs=[]
	for inputString in inputData:
		temp=inputString.strip()
		ext=temp.split(".")[-1]
		if ext=='c':
			result_c.append(temp)
		elif ext=='cs':
			result_cs.append(temp)
		elif ext=='cpp':
			result_cpp.append(temp)
	'''/**************Writing result to file*********************/'''

	output_c_file = open('c_'+file_object, 'w')
	output_cpp_file = open('cpp_'+file_object,'w')
	output_cs_file = open('cs_'+file_object,'w')
	for item in result_c:
		output_c_file.write("%s\n" % item)
        for item in result_cpp:
                output_cpp_file.write("%s\n" % item)
        for item in result_cs:
                output_cs_file.write("%s\n" % item)

	#print result_c,result_cpp,result_cs
if __name__=='__main__':
	file_object='test.txt'
	print solution(file_object)

