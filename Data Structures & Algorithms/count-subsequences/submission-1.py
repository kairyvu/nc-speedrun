class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        prev = [1] * (m + 1)
        curr = [0] * (m + 1)
        
        for i in range(n - 1, -1, -1):
            curr[m] = 0
            for j in range(m - 1, -1, -1):
                curr[j] = curr[j + 1]
                if s[j] == t[i]:
                    curr[j] += prev[j + 1]
            prev, curr = curr, prev
        return prev[0]