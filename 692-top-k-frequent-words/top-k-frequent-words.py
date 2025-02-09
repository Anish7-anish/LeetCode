class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for i in words:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        print(freq)
        heap = []
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        
        ans = []
        
        for i in range(k):
            i,j = heapq.heappop(heap)
            ans.append(j)
        
        return ans
        
        

        