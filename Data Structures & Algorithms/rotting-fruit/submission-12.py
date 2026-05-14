class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count, time = 0, 0
        q = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while fresh_count > 0 and q:
            curr_length = len(q)
            for i in range(curr_length):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh_count -= 1
            time += 1

        if fresh_count == 0:
            return time
        else:
            return -1