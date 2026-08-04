class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        previous_sum=self.fib(n-1)
        next_sum=self.fib(n-2)
        answer=previous_sum+next_sum
        return answer
        