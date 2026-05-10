class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict={}

        for i in range(len(nums)):
            val=target-nums[i]

            if val in sumDict:
                return [sumDict[val],i]
            sumDict[nums[i]]=i
        return False
        