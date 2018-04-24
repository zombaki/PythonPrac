class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """found=[]
        for i in nums:
            if not i in found:
                found.append(i)
            else:
                found.remove(i)
        return found[0]"""
        ans = nums[0]
        for num in nums[1:]:
            ans =ans^ num
            print ans
        return ans
