class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def ecud(point):
            x = point[0]
            y = point[1]
            return sqrt((x**2)+(y**2))

        ans = []

        for i in points:
            dis = ecud(i)
            ans.append((dis,i))
        
        heapq.heapify(ans)
        res = []
        for i in range(k):
            _,a = heapq.heappop(ans)
            res.append(a)
        
        return res


        