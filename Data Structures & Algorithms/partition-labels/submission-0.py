class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hsmap = {}

        for i, c in enumerate(s):
            hsmap[c] = i
        
        lastIndex = 0
        count = 0
        res = []
        for i, c in enumerate(s):
            lastIndex = max(lastIndex, hsmap[c])
            count += 1
            if i == lastIndex:
                res.append(count)
                count = 0

        return res