class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftProd=[0 for i in range(len(nums))]
        rightProd=[0 for i in range(len(nums))]

        leftProd[0],rightProd[-1]=1,1

        for i in range(1,len(nums)):
            leftProd[i]=nums[i-1]*leftProd[i-1]

        for i in range(len(nums)-2,-1,-1):
            rightProd[i]=nums[i+1]*rightProd[i+1]
        print(leftProd,rightProd)

        ret=[leftProd[i]*rightProd[i] for i in range(len(nums))]
        return ret

        
        