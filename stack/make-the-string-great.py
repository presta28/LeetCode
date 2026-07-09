class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch.lower()==stack[-1].lower() and ch!=stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        ans = ""
        for ch in stack:
            ans = ans+ch
        return ans