class Solution:
    def countSubstrings(self, s: str) -> int:
        palin_count = 0
        for i in range(len(s)):
            #odd substrings
            l, r = i, i
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                palin_count += 1
                l -= 1
                r += 1
            #even substrings
            l, r = i, i+1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                palin_count += 1
                l -= 1
                r += 1
        return palin_count
            