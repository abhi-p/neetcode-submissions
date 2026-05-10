class Solution:
    def findMin(self, nums: List[int]) -> int:
        #0,5,2
 
        #[3,4,5,6,1,2]

        low, high=0,len(nums)-1
        minNum=float('inf')
        while low<high:
            mid=low+(high-low)//2

            if nums[mid]<nums[high]:
                high=mid
            else:
                low=mid+1
        return nums[low]
            