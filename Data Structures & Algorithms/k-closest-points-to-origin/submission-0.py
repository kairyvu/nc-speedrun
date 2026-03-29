class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        def calDistanceReverse(x, y):
            return -(x**2 + y**2)
        
        for x, y in points:
            distance = calDistanceReverse(x, y)
            heapq.heappush(maxHeap, (distance, [x, y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [coor for _, coor in maxHeap]