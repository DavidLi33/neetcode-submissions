class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create max heap by multiplying stone weight by negative 1 so its "smallest value"
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # pops negative of two heaviest stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # second > first since stone weights are negative
            if second > first:
                # push first - second for difference
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])