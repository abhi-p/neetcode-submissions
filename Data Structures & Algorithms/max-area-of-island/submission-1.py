class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):

            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]!=1 :
                return 0
            grid[r][c]=-1
            return (1+ dfs(r,c+1)+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1))

        maxArr=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                currArr=0

                if grid[r][c]==1:
                    currArr+=dfs(r,c)
                maxArr=max(maxArr,currArr)
        return maxArr