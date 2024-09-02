class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counter = defaultdict(int)
        sounter = defaultdict(int)
        for i in s:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        for i in t:
            if i in sounter:
                sounter[i] += 1
            else:
                sounter[i] = 1
        
        for i in counter:
            if counter[i] != sounter[i]:
                return False
        return True
        
        