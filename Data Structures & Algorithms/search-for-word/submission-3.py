class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        def dfs(r, c, i):            
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visited.add((r, c))
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in visited:
                    if dfs(newR, newC, i + 1):
                        return True

            visited.remove((r, c))
            return False
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
