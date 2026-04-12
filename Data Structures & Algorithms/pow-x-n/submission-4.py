class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        N = abs(n)
        curr = x

        while N > 0:
            if N & 1:
                res *= curr
            
            curr *= curr
            N >>= 1
        
        return res if n >= 0 else 1 / res