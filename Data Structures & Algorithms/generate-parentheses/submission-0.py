class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(op, cl):
            if op == n and cl == n:
                res.append("".join(curr))
                return
            if op > n:
                return

            curr.append("(")
            backtrack(op + 1, cl)
            curr.pop()
            if op > cl:
                curr.append(")")
                backtrack(op, cl + 1)
                curr.pop()


        backtrack(0, 0)
        return res