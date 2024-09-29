class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        pal = ""
        digits = ['0','1','2','3','4','5','6','7','8','9']
        digits = set(digits)

        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (i in digits):
                pal = pal + str(i)

        i = 0
        j = len(pal)-1

        while i < j:
            if pal[i] == pal[j]:
                i += 1
                j -= 1
            else:
                return False

        return True
