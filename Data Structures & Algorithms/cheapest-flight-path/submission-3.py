class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, price in flights:
            adj[s].append((price, d))
        
        minHeap = [(0, src, k + 1)]
        visited = set()
        while minHeap:
            print(minHeap)
            price, s, left = heapq.heappop(minHeap)
            if left < 0:
                continue
            if s == dst:
                return price
            visited.add(s)
            for nextP, d in adj[s]:
                if d in visited:
                    continue
                heapq.heappush(minHeap, (price + nextP, d, left - 1))
        
        return -1