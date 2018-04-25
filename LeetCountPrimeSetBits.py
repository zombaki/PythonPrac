lass Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def isprime(n):
            """Returns True if n is prime."""
            if n==1:
                return False
            if n == 2:
                return True
            if n == 3:
                return True
            if n % 2 == 0:
                return False
            if n % 3 == 0:
                return False

            i = 5
            w = 2

            while i * i <= n:
                if n % i == 0:
                    return False

                i += w
                w = 6 - w
            return True
        res=[]
        for i in range (L,R+1):
            #print bin(i)
            res.append(bin(i).split('b')[1].count('1'))
        return sum([1 for x in res if isprime(x)])
        
