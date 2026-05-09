class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2) #Robbing 3rd house + 1st house or just 2nd house
            rob1 = rob2                #Move rob1 to 2nd house
            rob2 = temp                #Move rob2 to 3rd house
        return rob2