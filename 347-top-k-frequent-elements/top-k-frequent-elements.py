import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        heap = []
        ans = []

        for key,val in freq.items():
            heapq.heappush(heap, (-(val), key))

        print(heap)

        for i in range(k):
            (b, a) = heapq.heappop(heap)
            ans.append(a)
        
        return ans


            

