class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
            
        ROWS,COLS=len(grid),len(grid[0])
        def traverse(r,c,path):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==1 or (r,c) in path:
                return 0
            #print(r,c)
            if r==ROWS-1 and c==COLS-1:
                return 1

            path.add((r,c))
            count=0
            count=traverse(r+1,c,path) + traverse(r-1,c,path)+traverse(r,c+1,path)+traverse(r,c-1,path)
            # count+=traverse(r-1,c,path)
            # count+=traverse(r,c+1,path)
            # count+=traverse(r,c-1,path)

            path.remove((r,c))

            return count
        return traverse(0,0,set())


   