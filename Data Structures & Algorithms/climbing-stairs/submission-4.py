class Solution:
    def climbStairs(self, n: int) -> int:
        # Start from top of staircase
        if n == 0:
            return 0
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one