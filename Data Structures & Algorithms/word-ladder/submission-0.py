class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0

        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for ch in range(ord("a"), ord("z") + 1):
                        char = chr(ch)
                        if char == word[i]:
                            continue
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in wordDict and newWord not in visited:
                            visited.add(newWord)
                            q.append(newWord)             
            res += 1
        
        return 0