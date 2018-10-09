def longestConsecutive(nums):
	nums=set(nums)
	nums=list(nums)
	nums.sort(key=int)
	leng=len(nums)
	if len==0:
		return 0
	count=1;
	maxLen=1;
	print nums
	for i,a in enumerate (nums[:-1]):
		if a == (nums[i+1]-1):
			count+=1;
			maxLen=max(count,maxLen)
		else:
			count =1;
	return maxLen
print longestConsecutive([0,-1])
