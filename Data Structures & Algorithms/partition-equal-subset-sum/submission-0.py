class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp_set = set()
        dp_set.add(0)
        target = sum(nums) // 2

        # Start from back of list and each time, add that value to all existing values in the set
        # If target is found, return True, else False
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for val in dp_set:
                if (val + nums[i]) == target:
                    return True
                nextDP.add(val + nums[i])
                nextDP.add(val)
            dp_set = nextDP
        return False