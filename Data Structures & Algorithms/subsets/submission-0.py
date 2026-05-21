class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curSet,subset=[],[]
        def back_dfs(nums,curSet, subset,i):
            if i>=len(nums):
                return subset.append(curSet.copy())

            curSet.append(nums[i])

            back_dfs(nums,curSet,subset,i+1)

            curSet.pop()
            back_dfs(nums,curSet,subset,i+1)
        
        back_dfs(nums,curSet,subset,0)

        return subset