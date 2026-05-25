class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, grid):
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == '1':
                grid[row][col] = '0'
                dfs(row + 1, col, grid)
                dfs(row - 1, col, grid)
                dfs(row, col + 1, grid)
                dfs(row, col - 1, grid)

        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c, grid)
        return islands