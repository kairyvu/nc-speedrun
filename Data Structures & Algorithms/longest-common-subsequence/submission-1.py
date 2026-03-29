class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[j] == text2[i]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])
            prev = curr.copy()
        return curr[0]