class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(num for num in nums)

        longest=0
        currLen=1

        for num in nums:
            while num-1 in numSet:
                num-=1
                currLen+=1
            longest=max(currLen,longest)
            currLen=1
        return longest



