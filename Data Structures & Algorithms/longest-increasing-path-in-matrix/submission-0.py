class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            maxLength = 1
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and matrix[r][c] < matrix[newR][newC]:
                    maxLength = max(maxLength, 1 + dfs(newR, newC))
            memo[(r, c)] = maxLength
            return memo[(r, c)]
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                curr = dfs(r, c)
                if curr:
                    res = max(res, curr)
        return res