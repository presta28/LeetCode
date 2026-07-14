class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for i in range(len(s)):
            ch1=s[i]
            ch2=t[i]
            if ch1 in dict1 and dict1[ch1]!=ch2:
                return False
            else:
                dict1[ch1]=ch2
            if ch2 in dict2 and dict2[ch2]!=ch1:
                return False
            else:
                dict2[ch2]=ch1
        return True        
        