class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        def dfs(r,c):
            if r>=ROWS or c>=COLS or r<0 or c<0 or grid[r][c]==0:
                return 0

            dirs=[[0,1],[0,-1],[1,0],[-1,0]]
            grid[r][c]=0

            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)

            



        res=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] ==1:
                    area= dfs(r,c)
                    print(area)
                    res=max(area,res)

        return res