class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r=0,0
        maxProfit=-float('inf')
        minPrice=prices[0]
        while l<len(prices) and r<len(prices):
            profit=prices[r]-minPrice
            maxProfit=max(maxProfit,profit)

            if prices[r]<minPrice:
                l=r
                minPrice=prices[r]
            r+=1
        if maxProfit<=0:
            return 0
        print(minPrice)
        return maxProfit


