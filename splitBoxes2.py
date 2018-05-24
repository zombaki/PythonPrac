import sys
line=sys.stdin.readline()
#print line

[n, m, p] = line.split(" ")
n, m, p = int(n), int(m), int(p)
def rec_fun(n,m,p):
	#print n
	if n<=m :
		return 1
	else:
		count=0
		new_n=n//p
		#print 'this is range '
		#print range(p-1)
		for i in range(p-1):
			print 'value of i is %d with value %d'%(i,new_n)
			count+=rec_fun(new_n,m,p)
		count+=rec_fun(n-(new_n*(p-1)),m,p)
		#print n-(new_n*(p-1))
		return count
print rec_fun(n,m,p)
