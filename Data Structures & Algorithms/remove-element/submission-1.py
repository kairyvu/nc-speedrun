class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while True:
            while r >= 0 and nums[r] == val:
                r -= 1
            if l > r:
                break

            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        
        return l