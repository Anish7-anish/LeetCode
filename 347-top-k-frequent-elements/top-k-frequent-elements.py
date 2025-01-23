class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        heap = []
        
        for key,v in freq.items():
            heap.append((-v,key))
        heapq.heapify(heap)
        print(heap)
        
        res = []
        for i in range(k):
            print(i)
            _,ans = heapq.heappop(heap)
            res.append(ans)
        return res
        



        