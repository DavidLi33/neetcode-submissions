class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        # Bottom-up approach by starting at the end of the list
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                # Since we start from the back, we can only update if the next value is decreasing
                if nums[i] < nums[j]:
                    # lis[i] will continuously update so we don't have to do anything else
                    lis[i] = max(lis[i], 1+lis[j])
        return max(lis)