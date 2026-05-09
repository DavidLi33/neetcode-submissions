class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited, queue = set(), deque()
        # Store all treasure chest locations
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        # BFS code from treasure chests going outward
        def bfs(r, c):
            if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visited or grid[r][c] == -1:
                return 
            queue.append((r,c))
            visited.add((r,c))

        dist = 0
        # queue starts off with just treasure chests
        while queue:
            # Capture 1 level at a time
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                bfs(r-1, c)
                bfs(r+1, c)
                bfs(r, c-1)
                bfs(r, c+1)
            dist += 1