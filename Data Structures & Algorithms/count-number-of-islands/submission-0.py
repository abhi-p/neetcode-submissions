class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS,COLS=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]!="1":
                return
            dirs=[(0,1),(1,0),(-1,0),(0,-1)]
            grid[r][c]="X"
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                dfs(nr,nc)

            return 8



            

        

        numIslands=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1":
                    dfs(r,c)
                    numIslands+=1
        return numIslands
                
                
                


    