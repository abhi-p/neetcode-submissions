class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS,COLS=len(board),len(board[0]) 
        edgeOs=set()
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]

        def flagO(r,c):
            if (r,c) in edgeOs or r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O":
                return
            edgeOs.add((r,c))

            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                flagO(nr,nc)
            return
            


        for r in range(ROWS):
            if board[r][0] =="O":
                flagO(r,0)
            if board[r][COLS-1]=="O":
                flagO(r,COLS-1)

        for c in range(COLS):
            if board[0][c] =="O":
                flagO(0,c)
            if board[ROWS-1][c]=="O":
                flagO(ROWS-1,c)
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] =="O" and (r,c) not in edgeOs:
                    board[r][c]="X"
