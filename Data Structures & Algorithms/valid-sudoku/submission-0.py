class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = board[r][c]
                if cell == ".":
                    continue
                boxR, boxC = r // 3, c // 3
                if cell in rows[r] or cell in cols[c] or cell in boxes[(boxR, boxC)]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[(boxR, boxC)].add(cell)
        return True