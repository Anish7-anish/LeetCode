class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            key = tuple(count)
            if key in anagram_dict:
                anagram_dict[key].append(s)
            else:
                anagram_dict[key] = [s]
        
        l = []
        for i in anagram_dict.values():
            l.append(i)
        return l


            
        