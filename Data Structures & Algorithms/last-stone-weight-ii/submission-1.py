class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half = total // 2
        memo = {}

        def dfs(i, currSum):
            if currSum >= half or i >= len(stones):
                return abs(total - 2*currSum)
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            memo[(i, currSum)] = min(dfs(i + 1, currSum + stones[i]), dfs(i + 1, currSum))
            return memo[(i, currSum)]

        return dfs(0, 0)