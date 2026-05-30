class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo={}
        if not coins or min(coins)>amount:
            return 1
        coins.sort()
        def dp(index,value):
            if value>amount or index>=len(coins):
                return 0
            if value==amount:
                return 1
            
            
            if (index,value) in memo:
                return memo[(index,value)]

            ret=0
            if amount-value>=coins[index]:
                ret=dp(index+1,value)
                ret+=dp(index,value+coins[index])
            memo[(index,value)]=ret

            return memo[(index,value)]



        return dp(0,0) 

