class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            flg=True
            for x in str(i):
                if x == '0':
                    flg=False
                    break
                elif i%int(x):
                    flg=False
                    break
            if flg:
                res.append(i)
                
        return res
        
