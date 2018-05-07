class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        listLR=[]
        for a in grid:
            listLR.append(max(a))
        listTB=[]
        for i in range(len(grid[0])):
            temp=[]
            for b in grid:
                temp.append(b[i])
            #print temp
            listTB.append(max(temp))
        #print listTB
        sum=0
        for i in range(len(grid[0])):
            for b in range(len(grid)):
                sum+=(grid[i][b]-min(listLR[i],listTB[b]))
        return abs(sum)
                     
        
