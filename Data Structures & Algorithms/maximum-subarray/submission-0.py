class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        maxSub = nums[0]
        currSum = 0
        for num in nums:
            # If negative prefix sum before the current value, remove it since it 
            # only hurts us
            if currSum < 0:
                currSum = 0
            # Pick new starting point at this value
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub