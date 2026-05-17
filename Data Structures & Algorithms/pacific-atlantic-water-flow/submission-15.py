class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # Set of coords reachable by pacific/atlantic ocean
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r not in range(rows) or c not in range(cols) or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        # First row reachable with pacific and last row reachable with atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
    
        # Left col reachable with pacific and right col reachable to atlantic
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        # If position in both, we add it to our total result
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r,c))
        return res
