class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = suffix[len(suffix)-1] = 1

        # Fill prefix list values by starting from 1 since 0 index is already 1
        for i in range (1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Fill suffix list values by starting from second to last index and going to the first
        for i in range (len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range (len(res)):
            res[i] = prefix[i] * suffix[i]
        
        return res
            

