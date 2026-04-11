class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0
        while r < len(nums):
            nums[l] = nums[r]
            l += 1
            r += 1
            while r < len(nums) and nums[r] == nums[r - 1]:
                r += 1
        return l