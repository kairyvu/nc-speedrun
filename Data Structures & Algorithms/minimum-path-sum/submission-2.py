class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # dp = [float("inf")] * (cols + 1)
        # dp[cols - 1] = 0

        # for r in range(rows - 1, -1, -1):
        #     for c in range(cols - 1, -1, -1):
        #         value = grid[r][c]
        #         dp[c] = value + min(dp[c], dp[c + 1])
        # return dp[0]
        memo = {} # (r, c) -> int

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if r >= rows or c >= cols:
                return float("inf")
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return memo[(r, c)]
        return dfs(0, 0)
