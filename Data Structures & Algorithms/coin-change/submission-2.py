class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1) # temp max value
        dp[0] = 0                    # 0 ways to make amount 0 with coins value > 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:         # coin value must be less than amount so it can take part
                    dp[a] = min(dp[a], 1+dp[a-c])  # potential solution
        
        if dp[amount] == amount+1:   # Nothing valid
            return -1
        else:
            return dp[amount]