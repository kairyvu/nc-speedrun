class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    l += 1

        return res