"""
## A python program to compare the two version numbers. 
## Assumption 1 - The version strings are non-empty and contain only digits and the . character. 
## Assumption 2 - The . character does not represent a decimal point and is used to separate number sequences.
## Examples  ##
0.1 < 1.1 < 1.2 < 13.37 
1 < 2
1.1 < 1.1.2
1.0.0.0 = 1.0
2.0 < 10.0 

Output possibilites 1 if: version1 > version2, -1 elif version1 < version2, else  0

Input - Strings
Output - Integer


"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #spliting both the strings on the basis of "." and generating two lists
        list1=version1.split('.')
        list2=version2.split('.')
        
        #Compare the length of both the lists, and if lenth is not equal then add zeros to make the list size same
        if(len(list2)>len(list1)):
                list1=list1+['0']*(len(list2)-len(list1)) 
        elif(len(list1) > len(list2)):
                list2=list2+['0']*(len(list1)-len(list2))
        print list1,list2
	#loop to find the output by comparing at each iteration till the 
        
	#length of the list(any list as both have same length)		    
        for i in range(max(len(list1),len(list2))):
	    tempVer1=int(list1[i]) if i < len(list1) else 0
	    tempVer2=int(list2[i]) if i < len(list2) else 0
            if(tempVer1>tempVer2):
                return 1 
            elif(tempVer1<tempVer2):
                return -1        
        return 0



versions = [["1.0.0.0", "1.0"], ["1","2"], ["1.1","1.2"], ["2.0","1.1"], ["10.0.0.2","10.0.0.1"], ["1.2.1.2.3.3.1","1.2.2.1.2.1.2.1.2.1.1.1.2.1.2"], ["2.1.2","2.1.1.2"]] 
version1 = "10.0"
version2 = "10.0.0.1"
myclass= Solution()

for testCase in versions:
	print "Version 1 is %s \t\tVersion 2 is %s \t\tfunction gives us : %d"%(testCase[0],testCase[1],myclass.compareVersion(testCase[0],testCase[1]))
#print myclass.compareVersion(version1, version2)
