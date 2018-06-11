'''squares = {}
for x in range(6):
   squares[x] = x*x

print squares
'''
def allP(graph):
	"""
	:type graph: List[List[int]]
	:rtype: List[List[int]]
	"""
	val={}
	for index,val in enumerate (graph):
	    print index
	    val[index] = index
	print val

allP([[1,2],[3],[3],[]])
