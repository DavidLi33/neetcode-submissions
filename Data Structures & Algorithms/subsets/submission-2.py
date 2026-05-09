class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(index):
            # Base case
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # Include nums[index] in set
            subset.append(nums[index])
            dfs(index + 1)
            # Do not include nums[index] in set
            subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return res