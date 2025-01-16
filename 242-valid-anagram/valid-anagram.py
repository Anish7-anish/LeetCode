class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        
        for i in t:
            if i in freq:
                freq[i]-=1
            else:
                return False
        for i in freq:
            if freq[i]>0:
                return False
        return True
        