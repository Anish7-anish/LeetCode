class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)

        max_len = word1 if len(word1)>len(word2) else word2
        len_min=min(len1,len2)
        print("len_min",len_min)
        s=""
        for i in range(0,len_min):
            s+=word1[i]
            s+=word2[i]
        s+=max_len[(len(max_len)-abs((len1-len2))):]
        return s
        
        


        