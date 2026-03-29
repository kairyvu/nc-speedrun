class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((t, v))

        minHeap = [(0, k)]
        visited = set()
        res = 0

        while minHeap:
            t1, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            
            visited.add(u)
            res = max(res, t1)

            for t2, v in edges[u]:
                if v not in visited:
                    heapq.heappush(minHeap, (t1 + t2, v))
            
        return res if len(visited) == n else -1