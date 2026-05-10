class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
     

        def dfs(profit,weight,i,capacity):
            if i==len(profit):
                return 0

            maxProfit=dfs(profit,weight,i+1,capacity)

            newCap=capacity-weight[i]
            if newCap>=0:
                pKeep=profit[i]+dfs(profit,weight,i+1,newCap)
                maxProfit=max(maxProfit,pKeep)
            #print(i,newCap,maxProfit)
            return maxProfit
        return dfs(profit,weight,0,capacity)


#         capacity
#          0 1 2 3 4 5 6 7 8
# items  0[0 0 0 0 0 4 4 4 4]
#        1[0 0 4 4 4 4 4 8 8]
#        2[0 0 4 7 7 7 7 0 0]
#        3[0 0 0 0 0 0 0 0 0]
