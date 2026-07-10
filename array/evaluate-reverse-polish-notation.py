class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    ans = b + a

                elif tokens[i] == "-":
                    ans = b - a

                elif tokens[i] == "*":
                    ans = b * a

                else:
                    ans = int(b / a)

                stack.append(ans)
        return  stack.pop()