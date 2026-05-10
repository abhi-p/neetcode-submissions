class Solution:
    def trap(self, height: List[int]) -> int:\
    
        l,r=0,len(height)-1

        water=0
        maxL=-float('inf')
        maxR=-float('inf')
        storeL=[0 for _ in range(len(height))]
        storeR=[0 for _ in range(len(height))]

        for i in range(len(height)):
            if height[i]>maxL:
                maxL=height[i]
                continue
            storeL[i]=maxL-height[i]

        for i in range(len(height)-1,0,-1):
            if height[i]>maxR:
                maxR=height[i]
                continue
            storeR[i]=maxR-height[i]
    
        for i in range(len(storeL)):
            storeL[i]=min(storeL[i],storeR[i])

        return sum(storeL)





            

            


        