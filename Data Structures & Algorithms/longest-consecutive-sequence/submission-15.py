class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #immediately remove duplicates
        my_set = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in my_set:
                length = 1
                while num + length in my_set:
                    length += 1
                res = max(res, length)
        return res