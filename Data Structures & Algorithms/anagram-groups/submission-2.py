class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ret={}
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1

            if tuple(count) in ret:
                ret[tuple(count)].append(s)
            else:
                ret[tuple(count)]=[s]
        return list(ret.values())

