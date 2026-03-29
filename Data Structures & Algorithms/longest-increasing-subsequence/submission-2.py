class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        res = 0
        
        def findNextGreater(arr, target):
            l, r = 0, len(arr)
            while l < r:
                mid = (l + r) // 2
                if arr[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        for num in nums:
            index = findNextGreater(dp, num)
            if index == len(dp):
                dp.append(num)
                res += 1
            else:
                dp[index] = num
        return res