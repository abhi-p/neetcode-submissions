class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:


        memo={}

        def dfs(i,profit,weight,capacity):
            if i==len(profit):
                return 0
            if (i,capacity) in memo:
                return memo[(i,capacity)]

            
            memo[(i,capacity)]=dfs(i+1,profit,weight,capacity)

            newCap=capacity-weight[i]

            if newCap>=0:
                p=profit[i]+dfs(i,profit,weight,newCap)
                memo[(i,capacity)]=max(memo[(i,capacity)],p)

            return memo[(i,capacity)]


        return dfs(0,profit,weight,capacity)

