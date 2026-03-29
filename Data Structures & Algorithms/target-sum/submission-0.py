class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, target):
            if i == len(nums):
                if target == 0:
                    return 1
                return 0
            
            return dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])
        return dfs(0, target)