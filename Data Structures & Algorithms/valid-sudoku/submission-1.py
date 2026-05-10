class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS=[set() for i in range(len(board))]
        COLS=[set() for i in range(len(board))]
        BOXES=[set() for i in range(len(board))]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] !='.':
                    val=board[r][c]
                    if val in ROWS[r] or val in COLS[c] or val in BOXES[(r // 3) * 3 + (c // 3)]:
                        return False
                    ROWS[r].add(board[r][c])
                    COLS[c].add(board[r][c])
                    BOXES[(r // 3) * 3 + (c // 3)].add(board[r][c])



        return True