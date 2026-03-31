class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hsmap = {}

        for i, c in enumerate(s):
            hsmap[c] = i
        
        lastIndex = 0
        start = 0
        res = []
        for i, c in enumerate(s):
            lastIndex = max(lastIndex, hsmap[c])

            if i == lastIndex:
                res.append(i - start + 1)
                start = i + 1

        return res