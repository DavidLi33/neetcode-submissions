class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]                          #check rows
                    or board[r][c] in cols[c]                       #check cols
                    or board[r][c] in squares[(r // 3, c // 3)]     #check 3x3
                ):
                    return False
                #update corresponding rows, cols, and 3x3 squares
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
