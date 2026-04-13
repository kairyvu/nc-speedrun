class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == n:
                return [""]
            if i in memo:
                return memo[i]
            res = []
            for j in range(i, n):
                w = s[i:j+1]
                if w not in wordDict:
                    continue
                strings = dfs(j + 1)
                if not strings:
                    continue
                for string in strings:
                    sentence = w
                    if string:
                        sentence += " " + string
                    res.append(sentence)
            memo[i] = res
            return memo[i]
        
        return dfs(0)