class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def traverse(grid,r,c,path):
            ROWS=len(grid)
            COLS=len(grid[0])
            if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in path or grid[r][c]==1:
                return 0
            if r==ROWS-1 and c==COLS-1:
                return 1
            print("valid",r,c)
            path.add((r,c))
            print(path)
            count=0
            count+=traverse(grid,r+1,c,path)
            count+=traverse(grid,r,c+1,path)
            count+=traverse(grid,r-1,c,path)
            count+=traverse(grid,r,c-1,path)
            print("not possible, removing: ",r,c)
            path.remove((r,c))
            print(count)
            return count
        return traverse(grid,0,0,set())

