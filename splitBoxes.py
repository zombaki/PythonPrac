import sys
line=sys.stdin.readline()
print line

[n, m, p] = line.split(" ")
n, m, p = int(n), int(m), int(p)
equal_val=n//p
remain=n%p
stack=[]
stack.append(equal_val)
stack.append(equal_val+remain)
result=[]
while (stack):
	temp=stack.pop()
	print temp 
	if (temp//p>m):
		stack.append(temp//p)
		stack.append(temp-temp//p)
	else:
		result.append(temp//p)
		result.append(temp-temp//p)

if max(result)- min(result)>1:
	print len(result)+1
else:
	print len(result)
