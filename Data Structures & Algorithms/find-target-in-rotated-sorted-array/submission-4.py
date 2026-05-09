class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # In left portion
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    #Search right
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    #Search left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1








        # l = 0
        # r = len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[l] <= nums[mid]:                         #Left sorted portion
        #         if target > nums[mid] or target < nums[l]:
        #             l = mid + 1    #Search right
        #         else:
        #             r = mid - 1    #Search left
        #     else:
        #         if target < nums[mid] or target > nums[r]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # return -1