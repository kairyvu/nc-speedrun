class Solution:
    def checkPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def backtrack(i):
            if i == len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                string = s[i:j+1]
                if self.checkPalindrome(string):
                    curr.append(string)
                    backtrack(j + 1)
                    curr.pop()
        
        backtrack(0)
        return res