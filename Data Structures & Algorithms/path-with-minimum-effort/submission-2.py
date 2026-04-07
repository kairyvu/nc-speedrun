class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        minHeap = [(0, 0, 0)] # (diff, r, c)
        visited = set() # (r, c)

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if r == rows - 1 and c == cols - 1:
                return diff
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols:
                    newEdge = abs(heights[r][c] - heights[newR][newC])
                    heapq.heappush(minHeap, (max(diff, newEdge), newR, newC))