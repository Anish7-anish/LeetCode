class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        k={}
        counter = 0

        magazineset = list(set(magazine))
        ransomNoteset = list(set(ransomNote))
        for i in range(len(set(ransomNote))):
            for j in range(len(ransomNote)):
                if ransomNoteset[i] == ransomNote[j]:
                    counter+=1
            d[ransomNoteset[i]] = counter
            counter = 0

        for i in range(len(magazineset)):
            for j in range(len(magazine)):
                if magazineset[i] == magazine[j]:
                    counter+=1
            k[magazineset[i]] = counter
            counter = 0
        print(d)
        print(k)
        flag=0
        for i in d:
            print("d",d[i])
            if i in k and d[i] <= k[i]:
                flag=1
            else:
                return False
        if flag==1:
            return True

        