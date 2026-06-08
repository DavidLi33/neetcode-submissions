class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(n):
                if r <= n-1-r:
                    matrix[r][c], matrix[n-1-r][c] = matrix[n-1-r][c], matrix[r][c]
        
        for r in range(n):
            for c in range(n):
                if r < c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    