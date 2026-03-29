class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * m
        dp[-1] = 1

        for _ in range(n):
            for i in range(m - 2, -1, -1):
                dp[i] += dp[i + 1]
        return dp[0]