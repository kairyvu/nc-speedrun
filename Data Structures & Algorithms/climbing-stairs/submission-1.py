class Solution:
    def climbStairs(self, n: int) -> int:
        prev2Step, prev1Step = 0, 1
        res = 0

        for _ in range(n):
            res = prev2Step + prev1Step
            prev2Step, prev1Step = prev1Step, res    
        return res