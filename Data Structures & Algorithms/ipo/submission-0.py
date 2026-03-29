class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalProfit = [(c, p) for c, p in zip(capital, profits)]
        capitalProfit.sort()
        index = 0

        maxHeap = []
        while (maxHeap or index < len(capitalProfit)) and k > 0:
            while index < len(capitalProfit) and w >= capitalProfit[index][0]:
                heapq.heappush(maxHeap, -capitalProfit[index][1])
                index += 1
            if not maxHeap:
                break
            profit = -heapq.heappop(maxHeap)
            w += profit
            k -= 1
        
        return w