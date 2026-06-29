class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current_count=0
        for i in range(k):
            if s[i] in "aeiou":
                current_count+=1
        max_count=current_count
        for i in range(k,len(s)):
            current_count=0
            s=s[i:i+k]
            for ch in s:
                if ch in"aeiou":
                    current_count+=1
                else:
                    current_count-=1
                if current_count>max_count:
                    max_count=current_count
        return max_count     