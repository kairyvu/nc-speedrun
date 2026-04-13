class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = defaultdict(list) # index -> all possible strings
        wordDict = set(wordDict)
        n = len(s)
        res, curr = [], []
        
        def dfs(i):
            if i == len(s):
                res.append(" ".join(curr))
                return
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    curr.append(w)
                    dfs(j + 1)
                    curr.pop()
        
        dfs(0)
        return res