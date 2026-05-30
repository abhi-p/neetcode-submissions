class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}


        #In each day we have a few option

        #We can do nothing
        #If we already bought we can sell

        #If we sold

        def dp(day,canBuy):
            if day>=len(prices):
                return 0
            
            if (day,canBuy) in memo:
                return memo[(day,canBuy)]

            #skip the current day
            coolDown=dp(day+1,canBuy)

            if canBuy:
                buy=dp(day+1,not canBuy) -prices[day]
                memo[(day,canBuy)]=max(buy,coolDown)

            else:
                sell=dp(day+2,not canBuy)+prices[day]
                memo[(day,canBuy)]=max(coolDown,sell)

            return memo[(day,canBuy)]

        return dp(0,True)