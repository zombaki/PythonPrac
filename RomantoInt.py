class Solution(object):
    maplocal = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        if s=='':
            return 0
        else:
            sum=self.maplocal[s[len(s)-1]]
            #print len(s)
            for i in range(len(s)-1):
                #print i
                if(self.maplocal[s[i]]< self.maplocal[s[i+1]]):
                    sum -= self.maplocal[s[i]]
                else:
                    sum+=self.maplocal[s[i]]
            return sum
