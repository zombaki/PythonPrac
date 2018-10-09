def longestConsecutive(nums):
        nums=set(nums)
        leng=len(nums)
        if leng==0:
                return 0
        local=0;
        maxLen=1;
	y=list(nums)[0];
        print nums
        for x in nums:
		if x>y:
			continue
		local = x
		while local in nums:
			local+=1
		if maxLen<(local-x):
			maxLen=(local-x)
			y=x
		maxLen=max(maxLen,local-x)
        return maxLen
print longestConsecutive([0,-1,9,1,2])                                    
