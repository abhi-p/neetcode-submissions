class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqList={}
        count=[[] for i in range(len(nums)+1)]

        for num in nums:
            if num in freqList:
                freqList[num]+=1
            else:
                freqList[num]=1
        freqGroup={}

        for val in freqList:
            count[freqList[val]].append(val)
        num=0
        ret=[]
        print(count)
        for i in range(len(count)-1,-1,-1):
            if count[i]:
                for val in count[i]:
                    ret.append(val)
                    num+=1
                if num==k:
                    break
        return ret


        