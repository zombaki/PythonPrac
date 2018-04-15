def median(x):
	x.sort()
	l=len(x)
	if (l%2==0):
		return (x[l/2]+x[l/2 -1])/2.0
	else:
		return (x[l/2])
	return x
print median([1,3,4,2,5,6])
