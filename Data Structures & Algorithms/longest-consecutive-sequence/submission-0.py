class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 in numSet:
                continue
            diff = 1
            while num + diff in numSet:
                diff += 1
            res = max(res, diff)
        return res