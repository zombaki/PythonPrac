class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        res=[]
        i=[index for index, value in enumerate(S) if value == C]
        for l in range(len(S)):
            res.append(min(abs(d-l) for d in i))
        return res
