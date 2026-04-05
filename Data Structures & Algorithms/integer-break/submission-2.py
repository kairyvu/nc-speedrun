class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for total in range(2, n + 1):
            dp[total] = total if total != n else 0
            for num in range(1, total):
                dp[total] = max(dp[total], dp[total - num] * num)

        return dp[n]