class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [
            [0 for _ in range(amount + 1)] 
            for _ in range(len(coins) + 1)
        ]
        coins = sorted(coins)
        
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i+1][a] + dp[i][a-coins[i]]

        return dp[0][amount]
        