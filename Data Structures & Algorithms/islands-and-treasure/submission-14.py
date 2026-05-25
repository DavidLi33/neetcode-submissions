class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited, queue = set(), deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))
        
        def bfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            queue.append((r, c))
        
        distance = 0
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                r, c = queue.popleft()
                grid[r][c] = distance
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)
            distance += 1


