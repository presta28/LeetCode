class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1:
            return 1
        i=1
        while i*i<x:
            left = i
            right = i*2
            i=i*2
        ans = 0
        for i in range(left,right+1):
            if i*i<=x:
                ans = i
        return ans

            