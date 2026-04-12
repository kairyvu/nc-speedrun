class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, posDiag, negDiag = set(), set(), set()
        self.res = 0

        def backtrack(r):
            if r == n:
                self.res += 1
                return
            
            for c in range(n):
                if c not in cols and (r + c) not in posDiag and (r - c) not in negDiag:
                    cols.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    backtrack(r + 1)
                    cols.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
        
        backtrack(0)
        return self.res