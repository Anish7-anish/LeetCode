from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # l=[]
        # for i in strs:
        #     arr=[]
        #     arr=list(i)
        #     arr.sort()
        #     l.append("".join(arr))
        # print(l)
        
        # ans=[]
        # s=[]
        # for i in range(len(l)):
        #     item = [strs[j] for j in range(len(l)) if l[j] == l[i]]
        #     if not any(item == elem for elem in s):
        #         ans.append(item)
        #         s.append(item)
        # return ans

        anagram_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            anagram_dict[key].append(s)

        
        return anagram_dict.values()

