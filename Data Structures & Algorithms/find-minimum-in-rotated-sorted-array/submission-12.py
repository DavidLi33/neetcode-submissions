class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # sorted
            if nums[l] < nums[r]:
                res = min (res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return res

        # res = nums[0]
        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     if nums[l] < nums[r]:         #Subarray is sorted
        #         res = min(res, nums[l])
        #         break
        #                                   #Subarray is not sorted
        #     m = (l + r) // 2
        #     res = min(res, nums[m])
        #     if nums[m] >= nums[l]:        #Part of left sorted portion
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res
