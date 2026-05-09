class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curr, total):
            # If target reached, curr is solution => add to res and return
            if total == target:
                res.append(curr.copy())
                return
            # Out of bounds cases if index exceeds boundary of nums 
            if index >= len(nums) or total > target:
                return
            # Choose to add an occurence of nums[index] to solution
            curr.append(nums[index])
            # Increase total 
            dfs(index, curr, total + nums[index])
            # Don't choose to add an occurence of nums[index] to solution
            curr.pop()
            # Increase index to prevent repeat
            dfs(index + 1, curr, total)
        
        dfs(0, [], 0)
        return res