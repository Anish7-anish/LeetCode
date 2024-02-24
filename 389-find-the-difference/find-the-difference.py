class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1=list(s)
        t1=list(t)
        for i in s1:
            t1.remove(i)
        return t1[0]