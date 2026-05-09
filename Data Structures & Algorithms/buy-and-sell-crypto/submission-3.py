class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest: #Find the minimum, doesn't matter if a smaller value is found
                lowest = price #later since you can't use prices from before
            result = max(result, price - lowest)
        return result