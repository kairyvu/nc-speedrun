class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1
        t0, t1, t2 = 0, 1, 1

        for i in range(3, n + 1):
            tmp = t0 + t1 + t2
            t0, t1, t2 = t1, t2, tmp
        
        return t2