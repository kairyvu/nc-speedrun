class Solution:
    def longestPalindrome(self, s: str) -> str:

        def getLongestPalindrome(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j-1
        
        res = ""
        for i in range(len(s)):
            p1, p2 = getLongestPalindrome(s, i, i)
            if p2 - p1 + 1 > len(res):
                res = s[p1:p2+1]
            p1, p2 = getLongestPalindrome(s, i, i + 1)
            if p2 - p1 + 1 > len(res):
                res = s[p1:p2+1]
        return res