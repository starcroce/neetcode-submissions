class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, res = prices[0], 0
        for p in prices:
            min_price = min(min_price, p)
            res = max(res, p - min_price)
        return res
