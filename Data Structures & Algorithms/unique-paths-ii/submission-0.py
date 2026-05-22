class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        memo={}
        ROWS,COLS=len(obstacleGrid),len(obstacleGrid[0])
        def dp(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r>=ROWS or c>=COLS or obstacleGrid[r][c]==1:
                return 0
            if r==ROWS-1 and c==COLS-1:
                return 1

            memo[(r,c)]=dp(r+1,c)+dp(r,c+1)

            return memo[(r,c)]

        return dp(0,0)
        