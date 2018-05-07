import types
def flatten_list(nested_list):
	result=[]
	if isinstance(nested_list,int):
		#print 'inside recurr \t'+ str(nested_list)
		result.append(nested_list)
		return result
	
	for a in nested_list:
		#result.append(a)
		temp= flatten_list(a)
		#print temp
		result.extend(temp)
		#result.append(flatten_list(a))
	return result

if __name__=='__main__':
	print flatten_list([1,2,[3,4,[5]]])
