class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1Dict=[0]*26
        w2Dict=[0]*26

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            w1Dict[ord(s[i])-ord('a')]+=1        
            w2Dict[ord(t[i])-ord('a')]+=1        

        if w1Dict==w2Dict:
            return True
        return False