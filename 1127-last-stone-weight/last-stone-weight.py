class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        print(stones)

        while len(stones)>1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones,-(y-x))
        
        if len(stones)==0:
            return 0
        else:
            return -stones[0]
            
            


        