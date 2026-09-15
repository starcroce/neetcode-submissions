class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        row, col = len(s1), len(s2)
        dp = [
            [False for _ in range(col + 1)]
            for _ in range(row + 1)
        ]
        dp[0][0] = True

        for i in range(1, row + 1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]

        for j in range(1, col + 1):
            dp[0][j] = dp[0][j-1] and s3[j-1] == s2[j-1]
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                end_s1 = dp[i-1][j] and s3[i+j-1] == s1[i-1]
                end_s2 = dp[i][j-1] and s3[i+j-1] == s2[j-1]
                dp[i][j] = end_s1 or end_s2

        return dp[-1][-1]