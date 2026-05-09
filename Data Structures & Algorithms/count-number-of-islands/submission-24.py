class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, grid):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return 
            grid[r][c] = "0"
            dfs(r+1, c, grid)
            dfs(r-1, c, grid)
            dfs(r, c+1, grid)
            dfs(r, c-1, grid)

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col, grid)
        return islands