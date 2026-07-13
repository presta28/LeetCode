class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack= []
        for num in arr:
            alive = True
            while stack and stack[-1]>0 and num<0:
                if abs(num)>stack[-1]:
                    stack.pop()
                elif stack[-1] == abs(num):
                    stack.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break
            if alive:
                stack.append(num)
        return stack