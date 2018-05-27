import math
import sys
def cutSticks(lengths):
	result=[]
	total_len=lengths.pop(0)
	while(lengths):
	#for a in range (12):
		result.append(len(lengths))
		minVal=min(lengths)
		lengths[:]=[x-minVal for x in lengths]
		lengths=filter(lambda a: a != 0, lengths)

		#print lengths
	return result

print cutSticks([4,1,1,2,3])
