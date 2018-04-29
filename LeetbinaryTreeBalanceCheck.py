# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,root):
        if not root:
            return 1,True
        else:
            leftH,lbl=self.helper(root.left)
            rightH,rbl=self.helper(root.right)
            if (abs(leftH-rightH)>1):
                return 0,False
            else:
                return max(leftH,rightH)+1 ,lbl and rbl 
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[1]
        
