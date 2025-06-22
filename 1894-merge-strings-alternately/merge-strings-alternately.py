class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        min_len = min(len_word1,len_word2)
        ans = ""

        for i in range(min_len):
            ans+=word1[i]+word2[i]
        
        if len_word1 > len_word2:
            ans+=word1[min_len:]
        else:
            ans+=word2[min_len:]
        return ans
        