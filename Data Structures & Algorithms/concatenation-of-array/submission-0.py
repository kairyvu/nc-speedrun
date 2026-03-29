class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums = [0] * (len(nums) * 2)
        for i in range(len(nums)):
            newNums[i] = newNums[i + len(nums)] = nums[i]
        return newNums