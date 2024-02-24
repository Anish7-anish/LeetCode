class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        f=needle[0]
        if needle in haystack:
            for i in range(h-n+1):
                if haystack[i]==f and haystack[i:i+n]==needle:
                    return i
        else:
            return -1
            
        