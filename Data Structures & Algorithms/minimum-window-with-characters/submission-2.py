class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)>len(s):
            return ""

        tMap,curMap={},{}
        have,need=0,len(tMap)
     
        for c in t:
            tMap[c]=1+tMap.get(c,0)


        have,need=0,len(tMap)
        r,l=0,0
        res,minRes="",float("inf")

        for r in range(len(s)):
            c=s[r]
            curMap[c]=1+curMap.get(c,0)
            # print(curMap)
            if c in tMap and curMap[c]==tMap[c]:
                have+=1
                
            while need ==have:
                # print(l,r)
                lc=s[l]
                if minRes>r-l+1:
                    minRes=r-l+1
                    res=s[l:r+1]
                curMap[lc]-=1
                if lc in tMap and curMap[lc]<tMap[lc]:
                    have-=1
                l+=1

                
        
        # print(res)
        # print(have)
        # print(tMap,curMap)
            
        return res







