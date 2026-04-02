class Solution:
    def checkValidString(self, s: str) -> bool:
        leftP, star = [], []

        for i in range(len(s)):
            if s[i] == "(":
                leftP.append(i)
            elif s[i] == "*":
                star.append(i)
            else:
                if leftP:
                    leftP.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while leftP and star:
            if leftP.pop() > star.pop():
                return False
        return not leftP