class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        # Default value
        res = nums[0]
        while l <= r:
            # If l=>r section sorted, compare left value with pre-existing res value
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                # In left sorted section => Must go right
                l = mid + 1
            else:
                r = mid - 1
            
        return res