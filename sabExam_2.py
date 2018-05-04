def listPairJoins(list1,list2):
	a=set()
	res=[]
	a.update(list1)
	a.update(list2)
	la=list(a) 
	for i,x in enumerate (la[:-1:]):
		print i,x
		if x+1==la[i+1]:
			#res.append("(%d,%d)"%(x,la[i+1]))
			ll=list()
			ll.append(x)
			ll.append(la[i+1])
			res.append(ll)
	return res

l1=[1,3,-5,16,8,15]
l2=[-4,9,-4,13,12]
print listPairJoins(l1,l2)
	

