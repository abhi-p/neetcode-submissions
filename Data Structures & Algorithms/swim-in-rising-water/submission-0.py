class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
       
        minHeap=[[grid[0][0],0,0]]
        visit=set()
        ROWS,COLS=len(grid),len(grid[0])
        dirs=[(0,1),(-1,0),(1,0),(0,-1)]
        visit.add((0,0))
        while minHeap:
            w1,r1,c1=heapq.heappop(minHeap)
            if r1==ROWS-1 and c1==COLS-1:
                return w1
            for dr,dc in dirs:
                nr,nc=r1+dr,c1+dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visit:
                    continue
        
                visit.add((nr,nc))
                heapq.heappush(minHeap,[max(w1,grid[nr][nc]),nr,nc])


        return -1
