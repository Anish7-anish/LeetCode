class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x,y = points[i][0],points[i][1]
            val = math.sqrt(x**2+y**2)
            heap.append((val,points[i]))
        
        heapq.heapify(heap)
        
        ans = []
        for i in range(k):
            val, point = heapq.heappop(heap)
            ans.append(point)
        
        return ans
        