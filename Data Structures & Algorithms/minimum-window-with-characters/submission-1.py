class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        have, need = 0, len(count)
        index, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            if s[r] not in count:
                continue
            count[s[r]] -= 1
            if count[s[r]] == 0:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    index = [l, r]
                    resLen = r - l + 1
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        have -= 1
                l += 1
        l, r = index
        return s[l:r+1] if resLen != float("inf") else ""