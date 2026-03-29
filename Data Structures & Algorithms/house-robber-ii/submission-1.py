class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def houseRobber(nums):
            prev2, prev1 = 0, 0
            for i in range(len(nums)):
                temp = max(prev2 + nums[i], prev1)
                prev2 = prev1
                prev1 = temp
            return prev1

        return max(houseRobber(nums[:len(nums) - 1]), houseRobber(nums[1:]))