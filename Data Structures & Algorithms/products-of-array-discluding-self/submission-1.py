class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,4,6]
        # [1 , 1,2,8]
        # [48,24,6,1]

        leftMult=[1]*len(nums)
        rightMult=[1]*len(nums)

        for i in range(1,len(nums)):
            leftMult[i]=leftMult[i-1]*nums[i-1]
            rightMult[len(nums)-1-i]=rightMult[len(nums)-i]*nums[-i]

        ret=[0]*len(nums)
        # print(leftMult,rightMult)
        for i in range(len(nums)):
            # print(i,ret[i],leftMult[i],rightMult[i])
            ret[i]=leftMult[i]*rightMult[i]

        return ret