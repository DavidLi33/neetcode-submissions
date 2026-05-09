class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_val = float('inf')

        for price in prices:
            if price < min_val:
                min_val = price
            res = max(res, price-min_val)
        return res
