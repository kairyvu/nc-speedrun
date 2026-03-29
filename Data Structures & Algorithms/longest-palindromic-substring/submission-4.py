class Solution:
    def longestPalindrome(self, s: str) -> str:

        def getLongestPalindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j-1
        
        l, r = 0, 0
        for i in range(len(s)):
            p1, p2 = getLongestPalindrome(i, i)
            if p2 - p1 > r - l:
                l, r = p1, p2
            p1, p2 = getLongestPalindrome(i, i + 1)
            if p2 - p1 > r - l:
                l, r = p1, p2
        return s[l:r+1]