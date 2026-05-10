class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(index,target):
            targetSum={}
            retArr=[]

            l,r=index+1,len(nums)-1

            while l<r:
                tarSum=nums[l]+nums[r]
                if tarSum==target:
                    retArr.append([nums[index],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif tarSum<target:
                    l+=1
                else:
                    r-=1

            return retArr


        ret=[]
        for i in range(len(nums)):
            if i> 0 and nums[i]==nums[i-1]:
                continue
            pairs=twoSum(i,-nums[i])
         #   print("pairs",pairs)
            for pair in pairs:
                #print(pair)
                ret.append(pair)
                #print(ret)
        #print(ret)
        return ret

