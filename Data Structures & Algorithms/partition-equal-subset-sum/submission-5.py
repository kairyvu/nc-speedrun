class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(n):
            for j in range(target, 0, -1):
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]