class Solution:
    def simplifyPath(self, path: str) -> str:
        pathList = path.split("/")
        stack = []

        for p in pathList:
            if not p or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)