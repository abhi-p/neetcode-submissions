class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        
        for s in strs:
            arr=[0]*26
            for i in range(len(s)):
                arr[ord(s[i])-ord('a')]+=1
            
            arr=tuple(arr)
            if arr in groups:
                groups[arr].append(s)
            else:
                groups[arr]=[s]
        ret=[]

        for group in groups:
            val=[]
            for word in groups[group]:
                val.append(word)
            ret.append(val)
        return ret