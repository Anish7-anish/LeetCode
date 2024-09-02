class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        sounter={}

        for i in magazine:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for j in ransomNote:
            if j in sounter:
                sounter[j] += 1
            else:
                sounter[j] = 1

        print(counter)
        print(sounter)
        # flag=0
        # for i in sounter:
        #     if i in counter and sounter[i] <= counter[i]:
        #         flag=1
        #     else:
        #         return False
        # if flag==1:
        #     return True
        for i in ransomNote:
            if i not in counter:
                return False
            elif counter[i] == 1:
                del counter[i]
            else:
                counter[i]-= 1
        return True


        