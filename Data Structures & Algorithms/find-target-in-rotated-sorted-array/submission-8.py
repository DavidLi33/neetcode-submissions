class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            # Left side
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    # Search right
                    l = mid + 1
                else:
                    # Search right
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    # Search left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1







      