class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        if len(s)==0 or len(s)==1:
            return len(s)

        maxLen=-float('inf')
        charSet=set()
        while l<len(s) and r<len(s):
            print(s[l:r])
            print(charSet)
            if l==0 and r==0:
                r+=1
                charSet.add(s[l])
                continue

            while s[r] in charSet:
                #print('hello')
                charSet.remove(s[l])

                l+=1
            charSet.add(s[r])

            maxLen=max(maxLen,len(charSet))
            r+=1

        return maxLen