class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def capture(r,c): 
            if r not in range(len(board)) or c not in range(len(board[0])) or board[r][c] != "O":
                return 
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-1, c)
            capture(r, c+1)
            capture(r, c-1)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r in [0, len(board)-1] or c in [0, len(board[0])-1]):
                    capture(r, c)
    
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"