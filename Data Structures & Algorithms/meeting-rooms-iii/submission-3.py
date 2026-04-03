class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        counter = defaultdict(int)
        
        minHeap = [] # (endTime, room)
        for i in range(n):
            minHeap.append((0, i))
        heapq.heapify(minHeap)

        for start, end in meetings:
            while minHeap and minHeap[0][0] < start:
                endTime, room = heapq.heappop(minHeap)
                heapq.heappush(minHeap, (start, room))

            endTime, room = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (endTime + (end - start), room))
            counter[room] += 1            
        
        maxCount = max(count for count in counter.values())
        for i in range(n):
            if counter[i] == maxCount:
                return i
