class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        waitQueue = deque()
        maxHeap = [-val for val in counter.values()]
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or waitQueue:
            time += 1
            while waitQueue and time - waitQueue[0][0] > n:
                _, count = waitQueue.popleft()
                heapq.heappush(maxHeap, count)
            
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count < 0:
                    waitQueue.append((time, count))
        return time