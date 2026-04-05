class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # dp = [float("inf")] * (cols + 1)
        # dp[cols - 1] = 0

        # for r in range(rows - 1, -1, -1):
        #     for c in range(cols - 1, -1, -1):
        #         value = grid[r][c]
        #         dp[c] = min(value + dp[c], value + dp[c + 1])
        # return dp[0]
        memo = {} # (r, c) -> int

        def dfs(r, c):
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if r >= rows or c >= cols:
                return float("inf")
            if (r, c) in memo:
                return memo[(r, c)]
            value = grid[r][c]
            memo[(r, c)] = min(value + dfs(r + 1, c), value + dfs(r, c + 1))
            return memo[(r, c)]
        return dfs(0, 0)
