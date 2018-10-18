def returnCombination(deviceCap,b,c):
	result_local= [(b[i][0], c[j][0],b[i][1]+c[j][1]) for i in xrange(len(b)) for j in xrange(len(c))]
	result_local.sort(key=lambda x: x[2],reverse=True)
	res=[]
	localhigh=0
	for k, v,pri in result_local:
		if pri<=deviceCap:
			if localhigh<> 0 and pri == localhigh: 
				res.append([k,v])
			elif localhigh==0:
				res.append([k,v])
				localhigh=pri
			else:
				break
	return res
print returnCombination(10,[[1,2],[2,4],[3,6]],[[1,2],[2,6],[3,6]])
