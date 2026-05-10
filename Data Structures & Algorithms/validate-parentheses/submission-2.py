class Solution:
    def isValid(self, s: str) -> bool:
        openSet={'(':')','{':'}','[':']'}
        stack=[]
        for i in range(len(s)):
            if s[i] in openSet:
                stack.append(s[i])
            elif len(stack) and s[i] == openSet[stack.pop()]:
                continue
            else:
                return False
        return len(stack)==0

        