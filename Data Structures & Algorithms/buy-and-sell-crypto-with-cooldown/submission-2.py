class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        - if not buy -> (buy, skip)
        - if bought -> (sell, skip)
        - if sold -> (skip)

        dfs(index, have, allowToBuy)
        - dfs(index, True) -> dfs(index + 1, False) ; dfs(index + 1, True)
        - dfs(index, False) -> dfs(index + 1, False)
        '''
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            for allowToBuy in [True, False]:
                skip = dp[i + 1][allowToBuy]
                if allowToBuy:
                    dp[i][allowToBuy] = max(dp[i + 1][not allowToBuy] - prices[i], skip)
                else:
                    dp[i][allowToBuy] = max(dp[i + 2][not allowToBuy] + prices[i], skip)
        
        return dp[0][True]