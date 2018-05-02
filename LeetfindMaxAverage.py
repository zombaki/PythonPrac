class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg=0.0
        if k==1:
            return max(nums)
        for index,i in enumerate (nums[:-k+1:]):
            #print i,k
            val=sum(nums[index:index+k:])/float(k)
            avg=max(avg,val)
        return avg
