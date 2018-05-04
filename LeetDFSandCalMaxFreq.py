# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    counter=collections.defaultdict(int)
    def helper(self,root):
        if not root:
            return []
        else:
            self.counter[root.val]+=1
            self.helper(root.right)
            self.helper(root.left)
            return 0
            
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        maxfreq=max(self.counter.values())
        return [x for x,val in self.counter.items() if val==maxfreq ]
"""        if not root:
            return []

        queue = [root]
        mydir = {}
        res = []

        while queue:
            tempq = []
            for node in queue:
                mydir[node.val] = mydir.get(node.val, 0) + 1
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)
            queue = tempq

        maxfreq = max(mydir.values())
        for key, val in mydir.items():
            if val == maxfreq:
                res.append(key)
        return res"""      
