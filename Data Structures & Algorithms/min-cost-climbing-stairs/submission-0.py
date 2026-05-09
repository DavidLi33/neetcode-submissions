class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Add dummy 0 value
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            # Compare one jump and two jump results
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

        # Pick best starting point
        return min(cost[0], cost[1])