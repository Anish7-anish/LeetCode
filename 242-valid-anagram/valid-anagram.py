class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=list(s)
        t1=list(t)
        if len(s1)==len(t1):
            for i in s1:
                if i in t1:
                    t1.remove(i)
            if len(t1)==0:
                return True
        else:
            return False