class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(pos, curr, target):
            # Found correct result
            if target == 0:
                res.append(curr.copy())
            # Went over the target
            if target < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                # Prevents adding the same number multiple times (Don't choose 1 twice)
                if candidates[i] == prev:
                    continue
                # Choose the candidate
                curr.append(candidates[i])
                backtrack(i + 1, curr, target - candidates[i])
                # Don't choose the candidate
                curr.pop()
                prev = candidates[i]
        
        backtrack(0, [], target)
        return res