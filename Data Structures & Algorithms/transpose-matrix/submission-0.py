class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        res = [[0] * m for _ in range(n)]
        for r in range(n):
            for c in range(m):
                res[r][c] = matrix[c][r]
        return res