class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums), -1, -1):
            for j in range(i+1, len(nums)):
                #Check strictly increasing to see if we can extend length
                if nums[i] < nums[j]:
                    #lis[i] will continuously update so we don't have to do anything else
                    lis[i] = max(lis[i], 1+lis[j])
        return max(lis)