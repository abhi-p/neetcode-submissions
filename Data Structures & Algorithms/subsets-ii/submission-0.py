class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        curset,subset=[],[]

        nums.sort()
        def back_dfs(curset,subset,i):
            if i>=len(nums):
                subset.append(curset.copy())
                return

            curset.append(nums[i])
            back_dfs(curset,subset,i+1)
            curset.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            back_dfs(curset,subset,i+1)

        back_dfs(curset,subset,0)

        return subset