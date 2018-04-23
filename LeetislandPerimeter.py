class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        """def sum_adjacent(i, j):
            adjacent = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            res = 0
            for x, y in adjacent:
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
                    res += 1
            return res

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += sum_adjacent(i, j)
        return count"""
	"""        def adjacent(x,y):
            ad=(x-1,y),(x+1,y),(x,y-1),(x,y+1)
            res=0
            for xl,yl in ad:
                #print xl,yl,len(grid) 
                if (xl<0 or yl<0 or xl>=len(grid) or yl>=len(grid[0]) or grid[xl][yl]==0):
                    res+=1
            return res
        count =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]==1):
                    count+=adjacent(i,j)
        return count"""
	height = len(grid)
        width = len(grid[0])
        perimeter = 0
        
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    perimeter += 4
                    if y > 0 and grid[y - 1][x]:
                        perimeter -= 2
                    if x > 0 and grid[y][x - 1]:
                        perimeter -= 2
                        
        return perimeter
