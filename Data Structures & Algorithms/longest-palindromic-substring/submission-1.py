class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx, res_len = 0, 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if res_len < j - i + 1:
                        res_idx = i
                        res_len = j - i + 1

        return s[res_idx : res_idx + res_len]