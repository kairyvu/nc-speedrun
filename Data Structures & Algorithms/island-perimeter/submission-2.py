class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += (r + 1 >= rows or grid[r + 1][c] == 0)
                    res += (c + 1 >= cols or grid[r][c + 1] == 0)
                    res += (r - 1 < 0 or grid[r - 1][c] == 0)
                    res += (c - 1 < 0 or grid[r][c - 1] == 0)
        return res