class Solution:
    def longestPalindrome(self, s: str) -> str:

        def getLongestPalindrome(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j]
        
        res = ""
        for i in range(len(s)):
            palindrome = getLongestPalindrome(s, i, i)
            if len(palindrome) > len(res):
                res = palindrome
            palindrome = getLongestPalindrome(s, i, i + 1)
            if len(palindrome) > len(res):
                res = palindrome
        return res