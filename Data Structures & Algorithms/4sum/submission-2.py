class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, comb = [], []

        def getKSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    comb.append(nums[i])
                    getKSum(k - 1, i + 1, target - nums[i])
                    comb.pop()
                return
            
            l, r = start, len(nums) - 1
            while l < r:
                currSum = nums[l] + nums[r]
                if currSum < target:
                    l += 1
                elif currSum > target:
                    r -= 1
                else:
                    res.append(comb + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        getKSum(4, 0, target)
        return res