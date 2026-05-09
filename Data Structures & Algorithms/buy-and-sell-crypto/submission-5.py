class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        low = prices[0]
        for price in prices:
            if price < low:
                low = price
            result = max(price-low, result)
        return result