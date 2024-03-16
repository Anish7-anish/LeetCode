class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        print(s)

        # for i in s:
        #     if i == '':
        #         s.remove('')
        res = list(filter(('').__ne__, s))
        res=res[::-1]
        k=""
        for i in range(len(res)):
            if i==len(res)-1:
                k=k+res[i]
            else:
                k=k+res[i]
                k=k+" "
        return k
            
        