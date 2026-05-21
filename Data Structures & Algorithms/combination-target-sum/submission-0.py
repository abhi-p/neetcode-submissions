class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        curSet,subset=[],[]
        nums.sort()
        def back_dfs(curSum,curSet,i):
            if curSum==target:
                subset.append(curSet.copy())
                return
            if curSum>target or i>=len(nums):
                return
            curSet.append(nums[i])

            back_dfs(curSum+nums[i],curSet,i)
            curSet.pop()

            back_dfs(curSum,curSet,i+1)

        back_dfs(0,curSet,0)
        return subset