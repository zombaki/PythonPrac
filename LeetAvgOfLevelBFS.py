# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        """ans = []
        lvl = [root]
        while lvl:
            ans.append(sum(n.val for n in lvl) / float(len(lvl)))
            lvl = [c for n in lvl for c in [n.left, n.right] if c]
        return ans"""
        
        res=[]
        lvl=[root]
        while(lvl):
            res.append(sum(n.val for n in lvl)/float(len(lvl)))
            lvl=[x for d in lvl for x in [d.left,d.right] if x]
        return res
