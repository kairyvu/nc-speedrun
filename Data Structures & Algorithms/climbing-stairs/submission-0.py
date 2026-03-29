class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            prev = 0 if i < 2 else dp[i - 2]
            dp[i] = dp[i - 1] + prev
        return dp[n]