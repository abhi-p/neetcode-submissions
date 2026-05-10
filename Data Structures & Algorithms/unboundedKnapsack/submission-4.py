class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M =len(profit),capacity

        memo={}
        def dp(i,profit,weight,capacity):
            if i ==len(profit):
                return 0
            if (i,capacity) in memo:
                return memo[(i,capacity)]
            

            memo[(i,capacity)]=dp(i+1,profit,weight,capacity)

            newCap=capacity-weight[i]

            if newCap>=0:
                p=profit[i]+dp(i,profit,weight,newCap)
                memo[(i,capacity)]=max(p,memo[(i,capacity)])
            return memo[(i,capacity)]
        return dp(0,profit,weight,capacity)



