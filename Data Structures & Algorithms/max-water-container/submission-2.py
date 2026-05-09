class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        result = 0
        
        while l < r:
            temp_area = (r-l) * min(heights[l], heights[r])
            if temp_area > result:
                result = temp_area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result