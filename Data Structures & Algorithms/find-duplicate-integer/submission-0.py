class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            realNum = abs(num)
            if nums[realNum] < 0:
                return realNum
            nums[realNum] *= -1