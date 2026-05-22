class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        curSet,ret="",[]


        def back_dfs(i,curSet):
            if len(curSet)>i*2:
                return
            if i==n:
                while len(curSet)<n*2:
                    curSet=curSet+")"
                ret.append(curSet)
                return
            curSet=curSet+"("

            back_dfs(i+1,curSet)

            curSet=curSet[:-1]
            curSet=curSet+")"

            back_dfs(i,curSet)
            
        back_dfs(0,"")
        print(ret)
        return ret