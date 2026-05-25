class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col, grid):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row + 1, col, grid) + dfs(row - 1, col, grid) + dfs(row, col + 1, grid) + dfs(row, col - 1, grid)

        largest_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    largest_island = max(largest_island, dfs(r, c, grid))
        return largest_island
