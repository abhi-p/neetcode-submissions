class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqList={}
        for num in nums:
            freqList[num]=1+freqList.get(num,0)

        countList=[[] for _ in range(len(nums)+1)]

        for num in freqList:
            print(freqList[num])
            countList[freqList[num]].append(num)
        
        ret=[]
        seenFar=0
        for i in range(len(countList)-1,0,-1):
            if len(countList[i])>0:
                k-=len(countList[i])
                ret=ret+countList[i]
                if k<=0:
                    break
        
        return ret


            
        