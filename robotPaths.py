def numberOfPaths(m, n):
   # If either given row number is first
   # or given column number is first
   print m,n
   if(m == 1 or n == 1):
        return 1
   #print m,n
   # If diagonal movements are allowed
   # then the last addition
   # is required.
   return  numberOfPaths(m-1, n) + numberOfPaths(m, n-1)

m=3
n=2
print numberOfPaths(m,n)
