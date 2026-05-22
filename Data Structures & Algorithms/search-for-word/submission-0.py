class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS,COLS=len(board),len(board[0])
        dirs={(0,1),(1,0),(-1,0),(0,-1)}
        path=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c]!=word[i] or (r,c) in path:
                return False
            

            curLet=board[r][c]
            ret=False
            path.add((r,c))
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                ret= ret or dfs(nr,nc,i+1)
            path.remove((r,c))
            return ret

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False
            
