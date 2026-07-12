class Solution:
    def mySqrt(self, x: int) -> int:
        left =0
        while left<=x:
            ans = left*left
            if ans <= x:
                sqrt = left
            left+=1
        return sqrt
        