class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruit, time = 0, 0
        rotten_queue = collections.deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                if grid[r][c] == 2:
                    rotten_queue.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh_fruit > 0 and rotten_queue:
            queue_length = len(rotten_queue)
            for i in range(queue_length):
                row, col = rotten_queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        rotten_queue.append((new_row, new_col))
                        fresh_fruit -= 1
            time += 1

        if fresh_fruit == 0:
            return time
        else:
            return -1
        
