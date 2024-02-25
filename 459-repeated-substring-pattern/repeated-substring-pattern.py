class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss=s+s
        a=ss[1:len(ss)-1]
        print(a)
        if s in a:
            return True
        else:
            return False
        