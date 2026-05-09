class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited, queue = set(), deque()
        # Find all treasure chest locations and add to queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        # BFS code building levels from treasure chests
        def bfs(r, c):
            # Check if r and c are in range, if (r,c) are in visited, or water cell
            if r not in range(len(grid)) or c not in range(len(grid[0])) or (r,c) in visited or grid[r][c] == -1:
                return 
            queue.append((r,c))
            visited.add((r,c))

        dist = 0
        # Queue starts off with just treasure chests
        while queue:
            queue_len = len(queue)
            # Capture 1 level at a time fpr every treasure chest
            for i in range(queue_len):
                r, c = queue.popleft()
                grid[r][c] = dist
                bfs(r-1, c)
                bfs(r+1, c)
                bfs(r, c-1)
                bfs(r, c+1)
            dist += 1