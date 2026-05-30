class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo={}

        def dp(index,total):
            if index>len(nums) or (index==len(nums) and total!=target):
                return 0
            
            if index==len(nums) and total==target:
                return 1

            if (index,total) in memo:
                return memo[(index,total)]
            
            memo[(index,total)]=dp(index+1,total+nums[index])+dp(index+1,total-nums[index])
            return memo[(index,total)]
        return  dp(0,0)            
        