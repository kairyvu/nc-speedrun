class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0
        start = 0

        while count < n:
            currIndex = start
            prev = nums[start]
            while True:
                nextIndex = (currIndex + k) % n
                nums[nextIndex], prev = prev, nums[nextIndex]
                count += 1
                
                currIndex = nextIndex
                if currIndex == start:
                    break
            start += 1
