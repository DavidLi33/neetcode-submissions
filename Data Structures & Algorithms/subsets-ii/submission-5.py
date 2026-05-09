class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        subset = []
        def backtrack(index, subset):
            # Base case
            if index == len(nums):
                res.append(subset.copy())
                return 
            # Include nums[index] in set
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
            # Do not include nums[index] in set => skip duplicate values by moving index
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res