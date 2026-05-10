

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS=len(grid),len(grid[0])
        treasureChests=deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        visited=set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    treasureChests.append((r,c))
                    visited.add((r,c))

        while treasureChests:
            r,c=treasureChests.popleft()

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]==-1 or (nr,nc) in visited:
                    continue
                grid[nr][nc]=min(grid[nr][nc],grid[r][c]+1)
                treasureChests.append((nr,nc))
                visited.add((nr,nc))
                
                    
                    
