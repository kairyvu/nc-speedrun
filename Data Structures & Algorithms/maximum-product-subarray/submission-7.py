class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProduct = 1
        maxProduct = 1
        res = nums[0]
        
        for num in nums:
            temp = maxProduct
            maxProduct = max(num * temp, num * minProduct, num)
            minProduct = min(num * temp, num * minProduct, num)
            res = max(res, maxProduct)
        
        return res