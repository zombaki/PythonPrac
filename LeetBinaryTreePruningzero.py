# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val==0:
            templeft=self.pruneTree(root.left)
            tempright=self.pruneTree(root.right)
            if not templeft and not tempright:
                return None
            else:
                root.left=templeft
                root.right=tempright
                return root
        if root.val==1:
            root.left=self.pruneTree(root.left)
            root.right=self.pruneTree(root.right)
            return root
            
