class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2**31 - 1
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = 1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == INF:
                        grid[newR][newC] = dist
                        q.append((newR, newC))
            dist += 1