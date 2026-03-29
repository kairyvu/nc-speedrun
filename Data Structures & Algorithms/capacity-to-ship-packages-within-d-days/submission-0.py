class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def calDays(maxWeight):
            countDay = 1
            currWeight = 0
            for w in weights:
                currWeight += w
                if currWeight > maxWeight:
                    currWeight = w
                    countDay += 1
            return countDay <= days

        while l < r:
            mid = (l + r) // 2
            if calDays(mid):
                r = mid
            else:
                l = mid + 1
        
        return l