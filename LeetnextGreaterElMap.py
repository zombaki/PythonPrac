class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def helper(num):
            for tmp in nums[nums.index(num)::]:
                if (tmp>num):
                    return tmp
            return -1
        
        return map(helper,findNums)
