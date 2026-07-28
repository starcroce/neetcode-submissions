class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        # dp[i][0] is max profit can buy at day i
        # dp[i][1] is max profit can sell at day i
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[1][0] = max(-prices[0], -prices[1])
        dp[1][1] = max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1] - prices[i])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        return max(dp[-1])
            
                