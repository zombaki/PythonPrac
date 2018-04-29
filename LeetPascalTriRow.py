class Solution(object):
    def helper(self,row,lst):
        res=[]
        if row==0:
            return lst
        else:
            res.append(lst[0])
            for i in range(1,len(lst)):
                res.append(lst[i-1]+lst[i])
            res.append(lst[-1])
            return self.helper(row-1,res)
            
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.helper(rowIndex,[1])
