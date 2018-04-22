class Solution(object):
    code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morsE=[]        
        for i in words:
            morsword=''
            for w in i:
                morsword+=self.code[ord(w)-97]
            morsE.append(morsword)
        morsE=set(morsE)
        return len(morsE)
