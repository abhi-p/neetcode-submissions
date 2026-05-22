class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]

        dp[m-1][n-1]=1

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                dp[r][c]+=dp[r+1][c]+dp[r][c+1]
        
        return dp[0][0]

        
        # memo={}
        # ROWS,COLS=m,n
        # def dp(r,c):
        #     if (r,c) in memo:
        #         return memo[(r,c)]

        #     if r<0 or c<0 or r>=m or c>=COLS:
        #         return 0

        #     if r==m-1 and c==n-1:
        #         return 1



        #     memo[(r,c)]=dp(r+1,c)+dp(r,c+1)
        #     return memo[(r,c)]
        
        # return dp(0,0)
