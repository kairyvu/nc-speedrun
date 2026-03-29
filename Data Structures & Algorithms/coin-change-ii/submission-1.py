class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, a):
            if a == 0:
                return 1
            if (i, a) in memo:
                return memo[(i, a)]
            if i >= len(coins):
                return 0
            
            res = dfs(i + 1, a)
            if a - coins[i] >= 0:
                res += dfs(i, a - coins[i])
            memo[(i, a)] = res
            return memo[(i, a)]
        return dfs(0, amount)