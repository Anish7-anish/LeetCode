class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        traverse = word1 if len(word1)>=len(word2) else word2
        min_len = min(len(word1),len(word2))
        i = 0
        ans = ""

        while i < min_len:
            ans += word1[i]+word2[i]
            i=i+1

        for j in range(min_len,len(traverse)):
            ans += traverse[j]

        return ans
        

