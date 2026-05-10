class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M=len(profit),capacity
        dp=[[0]*(M+1) for _ in range(N)]

        for i in range(N):
            dp[i][0]=0
        for i in range(M+1):
            if weight[0]<=i:
                dp[0][i]=profit[0]
       
        for i in range(1,N):
            for cap in range(1,M+1):
                
                #if skiping val
                skip=dp[i-1][cap]
                include=0
                if cap-weight[i]>=0:
                    include=profit[i]+dp[i-1][cap-weight[i]]
                dp[i][cap]=max(skip,include)
        return dp[N-1][M]
#         capacity
#          0 1 2 3 4 5 6 7 8
# items  0[0 0 0 0 0 4 4 4 4]
#        1[0 0 4 4 4 4 4 8 8]
#        2[0 0 4 7 7 7 7 0 0]
#        3[0 0 0 0 0 0 0 0 0]
