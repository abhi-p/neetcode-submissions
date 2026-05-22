class Solution:
    def rob(self, nums: List[int]) -> int:

        memo={}
        def dp(house):
            if house>=len(nums):
                return 0

            if house in memo:
                return memo[house]
            
            maxLoot=max(dp(house+1),dp(house+2)+nums[house])
            memo[house]=maxLoot

            return memo[house]

        return dp(0)


        