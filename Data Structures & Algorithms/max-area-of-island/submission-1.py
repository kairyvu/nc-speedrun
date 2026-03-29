class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            grid[r][c] = 0
            total = 0
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 1:    
                    total += dfs(newR, newC)
            return 1 + total
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currArea = dfs(r, c)
                    res = max(res, currArea)
        return res