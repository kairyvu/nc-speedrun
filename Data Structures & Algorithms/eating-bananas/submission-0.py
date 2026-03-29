class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate, maxRate = 1, max(piles)

        def calculateHour(rate):
            hour = 0
            for p in piles:
                hour += (p + rate - 1) // rate
            return hour

        
        while minRate < maxRate:
            rate = (minRate + maxRate) // 2
            if calculateHour(rate) > h:
                minRate = rate + 1
            else:
                maxRate = rate
        return minRate