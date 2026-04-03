class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        counter = defaultdict(int)
        
        used = [] # (endTime, room)
        available = [i for i in range(n)]
        heapq.heapify(available)

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if not available:
                endTime, r = heapq.heappop(used)
                end = endTime + (end - start)
                heapq.heappush(available, r)

            newRoom = heapq.heappop(available)
            heapq.heappush(used, (end, newRoom))
            counter[newRoom] += 1
        
        maxCount = max(count for count in counter.values())
        for i in range(n):
            if counter[i] == maxCount:
                return i
