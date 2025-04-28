class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        heap = []
        for key,val in counter.items():
            heap.append((-val,key))
        
        heapq.heapify(heap)
        
        ans = []
        for i in range(k):
            val, key = heapq.heappop(heap)
            ans.append(key)
        
        return ans




            

        