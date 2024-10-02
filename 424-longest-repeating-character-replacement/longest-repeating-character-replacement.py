class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        n = len(s)
        l = 0
        counts = [0] * 26

        for r in range(n):
            counts[ord(s[r]) - ord('A')] += 1
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l+=1

            longest = max(longest, (r-l+1))
        return longest 
            
                