class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M =len(profit),capacity

        dp=[0]*(M+1)
        # for i in range(M+1):
        #     if i>=weight[0]:
        #         dp[i]=profit[0]
        print(dp)
        for i in range(N):
            currRow=[0]*(M+1)
            for c in range(1,M+1):
                skip=dp[c]
                include=0
                if c-weight[i]>=0:
                    include=profit[i]+currRow[c-weight[i]]
                currRow[c]=max(skip,include)
            dp=currRow
        return dp[M]
