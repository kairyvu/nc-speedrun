class Solution:
    def numDecodings(self, s: str) -> int:
        next1, next2 = 1, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                temp = 0
            else:
                temp = next1
            
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                temp += next2
            next2 = next1
            next1 = temp
        return next1
            