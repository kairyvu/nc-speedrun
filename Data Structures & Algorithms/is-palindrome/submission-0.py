class Solution:
    def isPalindrome(self, s: str) -> bool:
        evalLst = []
        for c in s:
            if c.isalnum():
                evalLst.append(c.lower())
        
        evalStr = "".join(evalLst)

        l, r = 0, len(evalStr) - 1
        while l < r:
            if evalStr[l] != evalStr[r]:
                return False
            l += 1
            r -= 1
        return True