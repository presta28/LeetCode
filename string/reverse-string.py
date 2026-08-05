class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1
        def reverse(left,right):
            if left>=right:
                return
            temp = s[left]
            s[left]=s[right]
            s[right]=temp
            reverse(left+1,right-1)
        reverse(left,right)

        """
        Do not return anything, modify s in-place instead.
        """
        