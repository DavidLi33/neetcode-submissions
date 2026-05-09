class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited, queue = set(), deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        def bfs(r, c):
            if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visited or grid[r][c] == -1:
                return 
            queue.append((r,c))
            visited.add((r,c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                bfs(r-1, c)
                bfs(r+1, c)
                bfs(r, c-1)
                bfs(r, c+1)
            dist += 1