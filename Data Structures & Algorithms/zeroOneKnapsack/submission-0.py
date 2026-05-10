class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N=len(profit)
        M=capacity
        cache=[[-1]*(M+1) for _ in range(N)]

        def dfsMemo(i,profit,weight,capacity,cache):
            if i==len(profit):
                return 0
            if cache[i][capacity]!=-1:
                return cache[i][capacity]

            #skip item
            cache[i][capacity]=dfsMemo(i+1,profit,weight,capacity,cache)

            #keep item:
            newCap=capacity-weight[i]

            if newCap>=0:
                p=profit[i]+dfsMemo(i+1,profit,weight,newCap,cache)
                cache[i][capacity]=max(cache[i][capacity],p)
            return cache[i][capacity]



        return dfsMemo(0,profit,weight,capacity,cache)