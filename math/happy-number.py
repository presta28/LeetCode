class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def issHappy(n:int,seen:set)->bool:
                if n==1:
                    return True
                total=0
                while n!=0:
                    rem = n % 10
                    total+=rem*rem
                    n=n//10
                if total not in seen:
                    seen.add(total)
                    return issHappy(total,seen)
                else:
                    return False
        return issHappy(n,seen)
                    
        



        