class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return checkPalindrome(l, r - 1) or checkPalindrome(l + 1, r)
            l += 1
            r -= 1
        return True