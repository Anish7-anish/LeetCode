class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] in freq:
                freq[ransomNote[i]]+=1
            else:
                freq[ransomNote[i]]=1
        freq_2 = {}
        for i in range(len(magazine)):
            if magazine[i] in freq_2:
                freq_2[magazine[i]]+=1
            else:
                freq_2[magazine[i]]=1

        print(freq)
        print(freq_2)
        
        for key,val in freq.items():
            if key not in freq_2 or freq_2[key]<val:
                return False
        return True