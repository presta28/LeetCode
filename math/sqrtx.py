# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x==0:
#             return 0
#         if x==1:
#             return 1
#         i=1
#         while i*i<x:
#             left = i
#             right = i*2
#             i=i*2
#         ans = 0
#         for i in range(left,right+1):
#             if i*i<=x:
#                 ans = i
#         return ans
#abbove is also correct
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2
        ans = 1

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid

            elif square < x:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans