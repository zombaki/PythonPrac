class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        """a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        print a
        res=[]
        for w in words:
            q=set(w.lower())
            if (q&a==q or q&b==q or q&c==q):
                res.append(w)
        return res
        """
        keys = [['q','w','e','r','t','y','u','i','o','p'],
                ['a','s','d','f','g','h','j','k','l'],
                ['z','x','c','v','b','n','m']]

        res = []
        for word in words:
            for key in keys:
                if set(word.lower()).difference(set(key)) == set([]):
                    res.append(word)
                    break
        return res
