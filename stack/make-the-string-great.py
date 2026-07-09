class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        for ch in s[1:]:
            if len(stack)!=0:
                if ch.lower()==stack[-1].lower() and ch!=stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        ans = ""
        for ch in stack:
            ans = ans+ch
        return ans