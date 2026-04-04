class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted((q, i) for i, q in enumerate(queries))
        res = [-1] * len(queries)
        minHeap = [] # (size, end)
        i = 0

        for q, q_i in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap:
                res[q_i] = minHeap[0][0]

        return res