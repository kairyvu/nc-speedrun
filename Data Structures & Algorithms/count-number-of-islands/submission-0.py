class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0"
            
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == "1":
                    dfs(newR, newC)
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res