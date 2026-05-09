class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                threesum = val + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skips over duplicate values on left side
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
            