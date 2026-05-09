class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, grid):
            # Bounds checking
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return 
            # Fill in current value as 0 to prevent loops
            grid[r][c] = "0"
            dfs(r-1, c, grid)
            dfs(r+1, c, grid)
            dfs(r, c-1, grid)
            dfs(r, c+1, grid)
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    # Add island and fill in adjacent part to prevent overcounting
                    res += 1
                    dfs(r, c, grid)
        return res