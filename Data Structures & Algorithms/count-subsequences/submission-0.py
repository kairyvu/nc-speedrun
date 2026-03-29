class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(m + 1):
            dp[n][i] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if s[j] == t[i]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]