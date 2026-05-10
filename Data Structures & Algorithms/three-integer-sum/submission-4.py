class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        def twoSum(index, target):
            sumDict={}
            curSum=set()

            for i in range(index,len(nums)):
                val=target-nums[i]

                if val in sumDict:
                    curSum.add(tuple([val,nums[i]]))
                sumDict[nums[i]]=i
            return curSum
            
        ret=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            retVal=twoSum(i+1,-nums[i])
            if retVal:
                for arr in retVal:
                    arr=list(arr)
                    arr.append(nums[i])
                    ret.append(arr)

        print(ret)
        return ret


