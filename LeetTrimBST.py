class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif (root.val>R):
            return self.trimBST(root.left,L,R)
        elif (root.val<L):
            return self.trimBST(root.right,L,R)
        
        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)
        return root
