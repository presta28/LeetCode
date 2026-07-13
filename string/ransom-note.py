class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_m = {}
        for ch in magazine:
            if ch not in freq_m:
                freq_m[ch]=1
            else:
                freq_m[ch]+=1
        found = True
        for ch in ransomNote:
            if ch in freq_m :
                if freq_m[ch]!=0:
                    freq_m[ch]-=1
                else:
                    return False
            else:
                return False
        return True


        