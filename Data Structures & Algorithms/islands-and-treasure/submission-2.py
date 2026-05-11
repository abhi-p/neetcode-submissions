class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        
        visit=set()
        que=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    que.append((r,c))
                    visit.add((r,c))


        while que:
            r,c=que.popleft()

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visit or grid[nr][nc]==-1:
                    continue
                grid[nr][nc]=min(grid[r][c]+1,grid[nr][nc])
                visit.add((nr,nc))
                que.append((nr,nc))

        
                    # [[4,-1,0,1],
                    # [3,2,1,-1],
                    # [1,-1,2,-1],
                    # [0,-1,3,4]]
 
                    #  [[3,-1,0,1],
                    #   [2,2,1,-1],
                    #   [1,-1,2,-1],
                    #   [0,-1,3,4]]

























