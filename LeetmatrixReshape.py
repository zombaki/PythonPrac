class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        """w=len(nums)
        l=len(nums[0])
        res=[[None]*c]*r
        if (r*c>l*w):
            return nums
        else:
            for i in range(l*w):
                res[int(i//c)][i%c]=nums[i//l][i%l]
        return res"""
        """flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
    
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)"""
        m=len(nums)
        n=len(nums[0])
        if r*c!=len(nums)*len(nums[0]):
            return nums
        newNums=[[] for i in  range(r)]
        for i in range(m):
            for j in range(n):
                    newNums[(i*n+j)//c].append(nums[i][j])
                
        return newNums
