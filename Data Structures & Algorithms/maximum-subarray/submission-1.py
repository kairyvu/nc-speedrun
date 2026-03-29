class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum