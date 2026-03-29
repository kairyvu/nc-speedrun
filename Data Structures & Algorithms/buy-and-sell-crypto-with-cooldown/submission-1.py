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
        memo = {}
        def dfs(index, allowToBuy):
            if index >= n:
                return 0
            if (index, allowToBuy) in memo:
                return memo[(index, allowToBuy)]
            skip = dfs(index + 1, allowToBuy)
            if allowToBuy:
                memo[(index, allowToBuy)] = max(dfs(index + 1, False) - prices[index], skip)
            else:
                memo[(index, allowToBuy)] = max(dfs(index + 2, True) + prices[index], skip)
            return memo[(index, allowToBuy)]
        return dfs(0, True)