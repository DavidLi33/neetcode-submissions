class Solution:
    def house_rob(self, num_list):
            rob1, rob2, = 0, 0
            for n in num_list:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.house_rob(nums[1:]), self.house_rob(nums[:-1]))