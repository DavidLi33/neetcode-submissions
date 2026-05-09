class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = defaultdict(int)
        left = 0
        max_count = 0

        for right in range(len(s)): 
            my_dict[s[right]] += 1
            max_count = max(max_count, my_dict[s[right]])
            if (right - left + 1) - max_count > k:
                my_dict[s[left]] -= 1
                left += 1
        return right - left + 1