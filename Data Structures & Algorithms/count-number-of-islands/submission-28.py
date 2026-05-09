class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        def dfs(r, c, grid, vist):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r,c) in vist or grid[r][c] == "0":
                return
            visit.add((r,c))
            dfs(r+1, c, grid, visit)
            dfs(r-1, c, grid, visit)
            dfs(r, c+1, grid, visit)
            dfs(r, c-1, grid, visit)

        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    islands += 1
                    dfs(r, c, grid, visit)
        return islands