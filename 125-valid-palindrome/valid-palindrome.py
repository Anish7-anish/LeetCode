class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        k=list(s)
        j=['0','1','2','3','4','5','6','7','8','9']
        k=[i for i in k if (ord(i)>96 and ord(i)<123) or (i in j)]
        print(k)
        
        l=0
        r=len(k)-1

        while(l<r):
            if k[l]!=k[r]:
                return False
            else:
                l+=1
                r-=1
        return True
        