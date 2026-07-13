class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        for ch in s:
            if ch not in freq:
                freq[ch]=1
            else:
                freq[ch]+=1
        ans = -1
        for ch in freq:
            if freq[ch]==1:
                ans = ch
                break
        sol=-1
        for i in range(len(s)):
            if ans==s[i]:
                sol=i
                break
        return sol
            
        

        