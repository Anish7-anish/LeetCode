class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        nums = ['0','1','2','3','4','5','6','7','8','9']
        s = list(s)
        filtered_s = [ch for ch in s if (96 < ord(ch) < 123) or (ch in nums)]
        st = "".join(filtered_s)
        print(st)
        l=0
        r=len(st)-1

        while(l<r):
            if st[l]!=st[r]:
                return False
            else:
                l+=1
                r-=1
        return True
