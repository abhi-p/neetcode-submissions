import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(k):
            hElapsed=0

            for bana in piles:
                hElapsed+=math.ceil(bana/k)

                if hElapsed>h:
                    return False
            return True


        low,high=1,max(piles)

        ret=max(piles)

        while low<=high:
            mid=low+(high-low)//2

            canFinish=canEat(mid)
            #print(low,high,mid,canFinish)
            if canFinish==True:
                ret=min(ret,mid)
                high=mid-1
            else:
                low=mid+1

        return ret

        