class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["endOfWord"] = word
        
        visited = set()
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = []
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, curr):
            if "endOfWord" in curr:
                res.append(curr["endOfWord"])
                del curr["endOfWord"]
            
            visited.add((r, c))
            for dr, dc in dirs:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in visited and board[newR][newC] in curr:
                    backtrack(newR, newC, curr[board[newR][newC]])
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    backtrack(r, c, root[board[r][c]])
        return res