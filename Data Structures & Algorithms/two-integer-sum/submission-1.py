class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        targetNum={}

        for i in range(len(nums)):
            val=target-nums[i]
            if val in targetNum:
                return [targetNum[val],i]
            else:
                targetNum[nums[i]]=i
        return False
        