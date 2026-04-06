class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        
        def dfs(r, c):
            board[r][c] = "#"
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and board[newR][newC] == "O":
                    dfs(newR, newC)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        