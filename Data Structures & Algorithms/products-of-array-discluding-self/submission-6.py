class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        running_product = 1
        zero_count = 0
        for num in nums:
            if (num == 0):
                zero_count += 1
            else:
                running_product *= num
        
        if zero_count > 1:
            output = [0] * len(nums)
        elif (zero_count == 1):
            for i in range(len(nums)):
                if (nums[i] != 0):
                    output.append(0)
                else:
                    output.append(running_product)
        else:
            for i in range(len(nums)):
                output.append(int(running_product/nums[i]))
        return output