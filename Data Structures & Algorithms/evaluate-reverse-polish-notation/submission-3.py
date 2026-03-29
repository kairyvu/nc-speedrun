class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                nums.append(int(token))
            else:
                num2, num1 = nums.pop(), nums.pop()
                if token == "+":
                    nums.append(num1 + num2)
                elif token == "-":
                    nums.append(num1 - num2)
                elif token == "*":
                    nums.append(num1 * num2)
                elif token == "/":
                    nums.append(int(num1 / num2))
        return nums.pop()