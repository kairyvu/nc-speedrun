class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        currComp = []

        def backtrack(i):
            if i == len(nums):
                res.append(currComp.copy())
                return
            currComp.append(nums[i])
            backtrack(i + 1)
            currComp.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res