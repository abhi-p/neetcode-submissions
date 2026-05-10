class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M=len(profit),capacity

        memo=[[-1]*(M+1) for _ in range(N)]

        def dfs(i,capacity):
            if i==len(profit):
                return 0
            if memo[i][capacity] != -1:
                return memo[i][capacity]
            
            memo[i][capacity]= dfs(i+1,capacity)

            newCap=capacity-weight[i]
            if newCap>=0:
                p=profit[i]+dfs(i,newCap)

                memo[i][capacity]=max(memo[i][capacity],p)

            return memo[i][capacity]
        
        return dfs(0,capacity)