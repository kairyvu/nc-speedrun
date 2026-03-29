class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        nums.sort()

        def backtrack(i, target):
            if target == 0:
                res.append(comb.copy())
                return
            for j in range(i, len(nums)):
                if target - nums[j] < 0:
                    return
                comb.append(nums[j])
                backtrack(j, target - nums[j])
                comb.pop()

        backtrack(0, target)
        return res