class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                curr.append(nums[i])
                backtrack(curr, used)
                used[i] = False
                curr.pop()
        
        backtrack([], [False] * len(nums))
        return res