class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        repeat = 0

        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    repeat = repeat * 10 + int(s[i])
                    i += 1
                stack.append(repeat)
                repeat = 0
                continue
            elif s[i] != "]":
                stack.append(s[i])
            else:
                currString = []
                while stack[-1] != "[":
                    currString.append(stack.pop())
                stack.pop()

                time = stack.pop()
                stack.append(time * "".join(list(reversed(currString))))
            i += 1
        return "".join(stack)