class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftMaxHeap, -num)
        num = -heapq.heappop(self.leftMaxHeap)
        heapq.heappush(self.rightMinHeap, num)
        if len(self.leftMaxHeap) < len(self.rightMinHeap):
            num = heapq.heappop(self.rightMinHeap)
            heapq.heappush(self.leftMaxHeap, -num)

    def findMedian(self) -> float:
        if len(self.leftMaxHeap) > len(self.rightMinHeap):
            return -self.leftMaxHeap[0]
        return (-self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2
        