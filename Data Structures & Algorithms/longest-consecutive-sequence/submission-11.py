class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # my_set = set()
        # unique_nums = []
        # for num in nums:
        #     if (num not in my_set):
        #         unique_nums.append(num)
        #     my_set.add(num)
        # unique_nums.sort()
        # result = 1
        # temp = 1
        # for i in range(1, len(unique_nums)):
        #     if (unique_nums[i] - unique_nums[i-1] == 1):
        #         temp += 1
        #         result = max(result, temp)
        #     else:
        #         temp = 1
        # return result

        my_set = set(nums)
        result = 0

        for num in my_set:
            if (num-1) not in my_set:
                length = 1
                while (num+length) in my_set:
                    length += 1
                result = max(result, length)
        return result
