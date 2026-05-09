class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            temp_water = min(heights[l],heights[r]) * (r-l)
            max_water = max(max_water, temp_water)
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return max_water