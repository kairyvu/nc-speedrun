class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry > 0:
            digit1 = int(a[i]) if i >= 0 else 0
            digit2 = int(b[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry
            
            res.append(str(total & 1))
            carry = total >> 1

            i -= 1
            j -= 1
        
        res.reverse()
        return "".join(res)