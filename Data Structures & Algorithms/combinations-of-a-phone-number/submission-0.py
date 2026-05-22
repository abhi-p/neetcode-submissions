class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        letterMap={
            "2":["A","B","C"],
            "3":["D","E","F"],
            "4":["G","H","I"],
            "5":["J","K","L"],
            "6": ["M","N","O"],
            "7": ["P","Q","R","S"],
            "8": ["T","U","V"],
            "9": ["W","X","Y","Z"]
        }
        curStr=""
        ret=[]
        def back_dfs(i,curStr):
            if len(curStr)==len(digits):
                ret.append(curStr)
                return

            for c in letterMap[digits[i]]:
                back_dfs(i+1,curStr+c.lower())

        if digits:
            back_dfs(0,"")
        return ret
