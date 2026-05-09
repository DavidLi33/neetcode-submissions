class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1) # This makes array from 0-len(s)
        dp[len(s)] = True
        for i in range(len(s), -1, -1): # Start from the back
            for w in wordDict:
                # Check if i and word length are in bounds and if s substring = word
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w: 
                    # Use boolean result from previous index already made
                    dp[i] = dp[i+len(w)]
                if dp[i] == True:
                    break
        return dp[0]