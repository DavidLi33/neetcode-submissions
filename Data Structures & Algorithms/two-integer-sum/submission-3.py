class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # my_list = list()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             my_list = list((i,j))
        # return my_list
        my_map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if (difference in my_map):
                return list((my_map[difference], i))
            my_map[n] = i

        