class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = dict()
        for i, val in enumerate(nums):
            diff = target - val
            if diff in diff_dict:
                return [diff_dict[diff], i]
            diff_dict[val] = i

            