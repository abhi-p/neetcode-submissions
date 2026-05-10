class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i in range(len(nums)):
            add=target-nums[i]
            if add in seen:
                return [seen[add],i]
            seen[nums[i]]=i
        
        