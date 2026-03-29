class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        time = 0
        while q and count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        count -= 1
            time += 1
        
        return time if count == 0 else -1