class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = []
        self.k = k
        for num in nums:
            heapq.heappush(self.stream, num)
            if len(self.stream) > self.k:
                heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        if len(self.stream) > self.k:
            heapq.heappop(self.stream)
        return self.stream[0]