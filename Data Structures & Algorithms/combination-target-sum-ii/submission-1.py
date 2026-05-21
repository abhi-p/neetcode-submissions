class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        curset,res=[],[]

        candidates.sort()
        def back_dfs(curSum,curset,i):
            
            if curSum==target:
                res.append(curset.copy())
                return
            
            if curSum>target or i>=len(candidates):
                return
        
            curset.append(candidates[i])

            back_dfs(curSum+candidates[i],curset,i+1)
            curset.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            back_dfs(curSum,curset,i+1)


        back_dfs(0,curset,0)
        return res