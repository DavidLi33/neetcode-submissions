class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            #Exceed nums in array or total exceeds target
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        res = []
        dfs(0, [], 0)
        return res