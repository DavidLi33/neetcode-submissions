class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Heaviest stone => just multiplied by -1
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                # first. = -8, second = -7, actual weights are 8 and 7
                # push a value of -1 to refer to a value of 1, so first - second
                heapq.heappush(stones, first - second)
        # fix base case of no stones left
        stones.append(0)
        return abs(stones[0])