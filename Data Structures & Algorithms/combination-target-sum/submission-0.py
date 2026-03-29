class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i, target):
            if target == 0:
                res.append(comb.copy())
                return
            if target < 0 or i == len(nums):
                return
            
            comb.append(nums[i])
            backtrack(i, target - nums[i])
            comb.pop()
            backtrack(i + 1, target)

        backtrack(0, target)
        return res