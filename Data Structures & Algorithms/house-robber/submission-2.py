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

        Time: O(n)
        Space: O(n)

        '''
        prev2, prev1 = 0, 0

        for i in range(len(nums)):
            temp = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = temp

        return prev1