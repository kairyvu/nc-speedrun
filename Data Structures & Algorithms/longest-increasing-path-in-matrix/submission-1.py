class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        indegree = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < rows and 0 <= newC < cols and matrix[r][c] > matrix[newR][newC]:
                        indegree[r][c] += 1

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if indegree[r][c] == 0:
                    q.append((r, c))
        
        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < rows and 0 <= newC < cols and matrix[r][c] < matrix[newR][newC]:
                        indegree[newR][newC] -= 1
                        if indegree[newR][newC] == 0:
                            q.append((newR, newC))
            res += 1
        return res






