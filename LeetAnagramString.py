class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """if s[::].sorted() == t[::].sorted():
            return True
        else:
            return False"""
        dict1={}
        dict2={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]]+=1
            else:
                dict1[s[i]]=1
            if t[i] in dict2:
                dict2[t[i]]+=1
            else:
                dict2[t[i]]=1
        if dict1==dict2:
            return True
        else:
            return False

	if len(s) != len(t):
            return False
        return all(s.count(c)==t.count(c) for c in string.lowercase)
