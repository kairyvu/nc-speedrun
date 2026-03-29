class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)
            total += num
        
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum