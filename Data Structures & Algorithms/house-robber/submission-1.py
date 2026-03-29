class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        dp = []
        nums = [2,9,8,3,6]
        at position i

        at position i what is the max profit we can get
        - sum of money at i - 1
        - sum of money at i - 2 + nums[i]

        get the max() of the 2
        dp = [] # max sum if we rob the current


        '''
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [0] * n

        for i in range(len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]