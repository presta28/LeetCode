class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        left = 2
        right = num//2
        found = False
        while left<=right:
            mid=(left+right)//2
            square=mid*mid
            if square==num:
                return True
            elif square<num:
                left=mid+1
            else:
                right=mid-1
        return False 
        