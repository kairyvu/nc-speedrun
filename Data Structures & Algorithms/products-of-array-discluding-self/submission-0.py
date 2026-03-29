class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(n):
            prev = 1
            if i > 0:
                prev = prefix[i - 1]
            prefix[i] = prev * nums[i]
        
        for i in range(n - 1, -1, -1):
            prev = 1
            if i < n - 1:
                prev = suffix[i + 1]
            suffix[i] = prev * nums[i]
        
        res = [1] * n
        for i in range(n):
            prefProd = prefix[i - 1] if i > 0 else 1
            suffProd = suffix[i + 1] if i < n - 1 else 1
            res[i] = prefProd * suffProd
        return res
        