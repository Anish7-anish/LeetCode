class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            # Window is not valid
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            
            
            w = (r-l)+1
            longest = max(longest,w)
            sett.add(s[r])
        return longest
        