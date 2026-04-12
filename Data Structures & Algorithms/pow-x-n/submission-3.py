class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def getPow(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            
            res = getPow(x * x, n // 2)
            return res if n % 2 == 0 else x * res
        
        res = getPow(x, abs(n))
        return res if n >= 0 else 1 / res