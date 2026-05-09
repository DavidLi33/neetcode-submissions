class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        my_dict = defaultdict(int)

        for right in range(len(s)):
            my_dict[s[right]] += 1
            while my_dict[s[right]] > 1:
                my_dict[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res

