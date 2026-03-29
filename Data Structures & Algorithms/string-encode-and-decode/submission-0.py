class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            length = str(len(s))
            res.append(length + "#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            currLen = []
            while s[i] != "#":
                currLen.append(s[i])
                i += 1
            strLen = int("".join(currLen))
            i += 1
            currString = []
            while strLen > 0:
                currString.append(s[i])
                strLen -= 1
                i += 1
            res.append("".join(currString))
        return res