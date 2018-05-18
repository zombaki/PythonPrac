# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        """dummy = TreeNode(None)
        def d(root, nums):
            if not nums:
                return 
            i = nums.index(max(nums))
            root.val = max(nums)
            if nums[:i]:
                root.left = TreeNode(None)
                d(root.left, nums[:i])
            if nums[i+1:]:
                root.right = TreeNode(None)
                d(root.right, nums[i+1:])
        d(dummy, nums)
        return dummy"""
        tmp=TreeNode(None)
        def helper(root,nums):
            if not nums:
                return None
            root.val=max(nums)
            i=nums.index(root.val)
            #print i
            if nums[:i]:
                root.left=TreeNode(None)
                helper(root.left,nums[:i])
            if nums[i+1:]:
                root.right=TreeNode(None)
                helper(root.right,nums[i+1:])
        helper(tmp,nums)
        return tmp
            
                
