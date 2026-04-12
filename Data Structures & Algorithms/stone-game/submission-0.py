class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = max(piles[i] - dfs(i + 1, j), piles[j] - dfs(i, j - 1))
            return memo[(i, j)]
        
        return True if dfs(0, 0) > 0 else False