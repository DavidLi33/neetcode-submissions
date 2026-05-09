class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        j = 0
        for i,n in enumerate(nums):
            diff = target - n
            if diff in my_dict:
                j = my_dict[diff]
                break
            else:
                my_dict[n] = i
        return [j, i]

        