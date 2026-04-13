class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)

        def dfs(i):
            if i == n:
                return [""]
            
            res = []
            for j in range(i, n):
                w = s[i:j+1]
                for word in wordSet:
                    if w == word:
                        suffixes = dfs(j + 1)
                        for suffix in suffixes:
                            sentence = (w + " " + suffix).strip()
                            res.append(sentence)
            return res
        
        return dfs(0)