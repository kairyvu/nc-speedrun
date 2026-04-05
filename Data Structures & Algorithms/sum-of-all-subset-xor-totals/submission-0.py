class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        orAll = 0
        for num in nums:
            orAll |= num
        
        return orAll << (len(nums) - 1)