class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        orderIndex = {c: i for i, c in enumerate(order)}

        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2) or orderIndex[w1[j]] > orderIndex[w2[j]]:
                    return False
                elif orderIndex[w1[j]] < orderIndex[w2[j]]:
                    break
        return True