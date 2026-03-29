class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo = {}
        
        # def dfs(i, target):
        #     if i == len(nums):
        #         if target == 0:
        #             return 1
        #         return 0
        #     if (i, target) in memo:
        #         return memo[(i, target)]
        #     memo[(i, target)] = dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])
        #     return memo[(i, target)]
        # return dfs(0, target)

        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        return dp[n][target]
