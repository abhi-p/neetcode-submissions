class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charFreq={}
        for c in s:
            if c in charFreq:
                charFreq[c]+=1
            else:
                charFreq[c]=1
        for c in t:
            if c not in charFreq or charFreq[c]==0:
                return False
            charFreq[c]-=1
        return True
        