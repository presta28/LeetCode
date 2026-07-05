class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        parts = []
        current =""
        for ch in s:
            current+=ch
            if ch == '(':
                stack.append(ch)
            else:
                stack.pop()
            if len(stack)==0:
                parts.append(current)
                current = ""
        ans = ""
        for part in parts:
            ans += part[1:-1]
        return ans
        