class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        result_len = 0
        for i in range(len(s)):
            # for odd palindromes
            left, right = i, i
            # pointer bounds checking
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Know its a palindrome
                if right - left + 1 > result_len:
                    #retrieve substring from l => r
                    res = s[left:right+1]
                    result_len = right-left+1
                left -= 1
                right += 1
            #even length
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > result_len:
                    #retrieve substring from l => r
                    res = s[left:right+1]
                    result_len = right-left+1
                left -= 1
                right += 1
        return res

