class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r < len(matrix)-1-r:
                    matrix[r][c], matrix[len(matrix)-1-r][c], = matrix[len(matrix)-1-r][c], matrix[r][c]
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r > c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c] 
        