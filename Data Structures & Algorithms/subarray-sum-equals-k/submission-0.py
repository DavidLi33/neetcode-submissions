class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        pref_sums = {0: 1}
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            res += pref_sums.get(diff, 0)
            pref_sums[curr_sum] = 1 + pref_sums.get(curr_sum, 0)
        return res