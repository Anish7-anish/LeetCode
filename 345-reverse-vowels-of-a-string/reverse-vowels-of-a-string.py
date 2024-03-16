class Solution:
    def reverseVowels(self, s: str) -> str:
        v=["a","e","i","o","u","A","E","I","O","U"]
        
        s=list(s)
        a=[]
        for i in range(len(s)):
            if s[i] in v:
                a.append(s[i])
        a=a[::-1]
        print(a)
        i=j=0
        k=len(s)
        while(k>0):
            if s[i] in v:
                s[i]=a[j]
                j+=1
            i+=1
            k-=1
        b=""
        return "".join(s)

        

        