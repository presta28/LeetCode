class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        word = s.split()
        if len(p)!=len(word):
            return False
        dict1={}
        dict2={}
        for i in range(len(p)):
            ch1=p[i]
            ch2=word[i]
            if ch1 in dict1 and dict1[ch1]!=ch2:
                return False
            else:
                dict1[ch1]=ch2
            if ch2 in dict2 and dict2[ch2]!=ch1:
                return False
            else:
                dict2[ch2]=ch1
        return True        
        