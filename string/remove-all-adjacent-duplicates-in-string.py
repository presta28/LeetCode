class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ans = ""
        for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            elif stack[-1]==s[i]:
                top=stack.pop()
            else:
                stack.append(s[i])
        for i in range(len(stack)):
            ans = ans+stack[i]
        return ans
        