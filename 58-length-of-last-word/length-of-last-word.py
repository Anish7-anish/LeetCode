class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        d=len(s)-1
        while(True):
            if s[d]==" ":
                d-=1
            else:
                break
        for i in range(d,-1,-1):
            if s[i]!=" ":
                c+=1
            else:
                break
        return c




        