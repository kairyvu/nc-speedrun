class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        repeat = 0

        for i in range(len(s)):
            if s[i].isdigit():
                repeat = repeat * 10 + int(s[i])
            elif s[i] != "]":
                if repeat:
                    stack.append(repeat)
                    repeat = 0
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