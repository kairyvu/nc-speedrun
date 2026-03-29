class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        
        for i in range(n):
            prefix[i] = nums[i] + prefix[i - 1]
        
        def canSplit(maxSum):
            index = 0
            splitCount = 0
            while index < n:
                l, r = index, n - 1
                while l <= r:
                    mid = (l + r) // 2
                    subSum = prefix[mid] - (prefix[index - 1] if index > 0 else 0)
                    if subSum <= maxSum:
                        l = mid + 1
                    else:
                        r = mid - 1
                splitCount += 1
                index = l
                if splitCount > k:
                    return False
            return True
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if canSplit(mid):
                r = mid
            else:
                l = mid + 1
        return l