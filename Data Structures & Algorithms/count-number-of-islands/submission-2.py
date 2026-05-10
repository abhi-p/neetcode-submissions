class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS,COLS=len(grid),len(grid[0])

        def dfs(r,c):

        
            delta=[(0,1),(1,0),(-1,0),(0,-1)]
            grid[r][c]="X"
            for dr,dc in delta:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]!="1" :
                    continue

                if grid[nr][nc]=="1":
                    dfs(nr,nc)
        islands=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    islands+=1
                    dfs(r,c)
        return islands

        