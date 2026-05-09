class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index_dict:
                return [index_dict[diff], i]
            index_dict[nums[i]] = i
