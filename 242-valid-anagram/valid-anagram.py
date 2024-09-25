from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sfreq = defaultdict(int)
        tfreq = defaultdict(int)

        for i in s:
            if i in sfreq:
                sfreq[i] += 1
            else:
                sfreq[i] = 1
        
        for i in t:
            if i in tfreq:
                tfreq[i] += 1
            else:
                tfreq[i] = 1

        print(sfreq)
        print(tfreq)

        for i in s:
            if sfreq[i]!=tfreq[i]:
                return False
        
        return True

