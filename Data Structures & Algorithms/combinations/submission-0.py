class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []
        
        def backtrack(num, k):
            if k == 0:
                res.append(comb.copy())
                return
            if num > n:
                return

            for val in range(num, n + 1):
                comb.append(val)
                backtrack(val + 1, k - 1)
                comb.pop()
        
        backtrack(1, k)
        return res