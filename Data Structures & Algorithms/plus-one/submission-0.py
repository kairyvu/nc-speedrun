class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        extra = 1
        for i in range(len(digits) - 1, -1, -1):
            if extra == 0:
                return digits
            newSum = digits[i] + extra
            extra, digits[i] = newSum // 10, newSum % 10
        
        return [extra] + digits if extra == 1 else digits