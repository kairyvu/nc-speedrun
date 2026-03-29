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
            j = i
            while s[j] != "#":
                j += 1
            strLen = int(s[i:j])
            i = j + 1
            res.append(s[i:i+strLen])
            i = i + strLen
        return res