class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l,r=0,0
        s1Map={}

        if len(s1)>len(s2):
            return False

        for c in s1:
            if c not in s1Map:
                s1Map[c]=1
            else:
                s1Map[c]+=1

        k=len(s1)
        curMap={}
        for i in range(k):
            c=s2[i]
            
            if c in curMap:
                curMap[c]+=1
            else:
                curMap[c]=1
        if curMap==s1Map:
            return True
        

        for i in range(len(s2)-k):
            if s2[i+k] in curMap:
                curMap[s2[i+k]]+=1
            else:
                curMap[s2[i+k]]=1
            curMap[s2[i]]-=1

            if curMap[s2[i]]<=0:
                del curMap[s2[i]]

            
            if curMap==s1Map:
                return True
            # print(curMap,s1Map)
        return False
        
