class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = [] 
        for ch in s:
            if ch!='#':
                stack1.append(ch)
            else:
                if len(stack1) != 0:
                    stack1.pop()
        for ch in t:
            if ch!='#':
                stack2.append(ch)
            else:
                if len(stack2) != 0:
                    stack2.pop()
        if stack1==stack2:
            return True
        else:
            return False