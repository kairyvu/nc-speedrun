class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2

        memo = {}
        def dfs(i, target):
            if target < 0:
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            if i == len(nums):
                return target == 0
            
            memo[(i, target)] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            return memo[(i, target)]
        
        return dfs(0, half)