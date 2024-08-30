class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_k=list(s)
        t_k=list(t)
        i,j=0,0

        while(i<len(s) and j<len(t)):
            if s[i] == t[j]:
                s_k.remove(s[i])
                print(s_k)
                i=i+1
                print('i',i)
                j=j+1
                print("j",j)
            else:
                j=j+1
                print("j",j)
        if len(s_k)==0:
            return True
        else:
            return False

        