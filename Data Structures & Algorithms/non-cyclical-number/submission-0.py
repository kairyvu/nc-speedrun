class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n):
            res = 0
            while n:
                digit = n % 10
                digit **= 2
                res += digit
                n //= 10
            return res
        

        slow, fast = n, sumOfSquares(n)
        while slow != fast:
            fast = sumOfSquares(fast)
            fast = sumOfSquares(fast)
            slow = sumOfSquares(slow)
        return True if fast == 1 else False