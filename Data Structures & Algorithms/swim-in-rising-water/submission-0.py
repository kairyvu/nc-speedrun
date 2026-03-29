class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [(grid[0][0], 0, 0)] # (t, r, c)
        n = len(grid)
        time = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        
        while minHeap:
            val, r, c = heapq.heappop(minHeap)
            time = max(time, val)
            visited.add((r, c))
            if r == n - 1 and c == n - 1:
                return time
            for dr, dc in dirs:
                newR, newC = dr + r, dc + c
                if not 0 <= newR < n or not 0 <= newC < n or (newR, newC) in visited:
                    continue
                heapq.heappush(minHeap, (grid[newR][newC], newR, newC))

        return time    