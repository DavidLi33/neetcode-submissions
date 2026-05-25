class Solution:
    def climbStairs(self, n: int) -> int:
        # DP is more optimal since there are many repeat subproblems 
        # to reach a specific amount of steps 
        # No dp is O(2^n) but dp is O(n)
        second_to_last, last = 1, 1
        for i in range(n-1):
            temp = second_to_last
            second_to_last = second_to_last + last
            last = temp
        return second_to_last
        