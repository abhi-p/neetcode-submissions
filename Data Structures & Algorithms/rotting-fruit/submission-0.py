class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        que=deque()
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        unrotten=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    que.append((r,c,0))
                if grid[r][c]==1:
                    unrotten+=1
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        timeElapsed=0
        while que:
            r,c,time=que.popleft()

            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                ntime=time+1
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visit or grid[nr][nc]!=1:
                    continue
                visit.add((nr,nc))
                que.append((nr,nc,ntime))
                unrotten-=1
                timeElapsed=max(timeElapsed,ntime)
        if unrotten>0:
            return -1
        return timeElapsed
        






        
        

        