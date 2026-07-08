class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in num2:
            while stack and stack[-1]<num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        while stack:
            value = stack.pop()
            next_greater[value]=-1
        ans = []
        for num in num1:
            ans.append(next_greater[num])
        return ans


        