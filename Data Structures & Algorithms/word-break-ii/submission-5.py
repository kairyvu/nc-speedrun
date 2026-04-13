class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for j in range(i):
                word = s[j:i]
                if word in wordSet:
                    for sentence in dp[j]:
                        dp[i].append((sentence + " " + word).strip())
        
        return dp[n]