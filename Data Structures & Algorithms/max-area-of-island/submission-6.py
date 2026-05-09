class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        def dfs(r, c, grid):
            # Bounds checking
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            # Set to 0 so that there's no loop
            grid[r][c] = 0
            # Add 1's in every direction to get the max island
            return 1 + dfs(r+1, c, grid) + dfs(r-1, c, grid) + dfs(r, c+1, grid) + dfs(r, c-1, grid)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_island = max(max_island, dfs(r, c, grid))
        return max_island
