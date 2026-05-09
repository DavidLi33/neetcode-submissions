class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        current = float("inf")

        while (start < end):
            mid = start + (end - start) // 2
            current = min(current, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1

            else: 
                end = mid - 1
        
        return min(current, nums[start])
