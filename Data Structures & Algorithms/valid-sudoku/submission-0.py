class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows={}
        cols={}
        squares={}
        ROWS,COLS=len(board),len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                square=(c//3,r//3)

                if r not in rows:
                    rows[r]=set()
                if c not in cols:
                    cols[c]=set()
                if square not in squares:
                    squares[square]=set()
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[square]:
                    return False

                if board[r][c]!=".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[square].add(board[r][c])
        return True

            


                



        