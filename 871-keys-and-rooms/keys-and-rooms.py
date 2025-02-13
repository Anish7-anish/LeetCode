class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        stk = [0]
        visited = set()
        keys = set([0])

        while stk:
            cur = stk.pop()
            visited.add(cur)
            for nei in rooms[cur]:
                if nei not in visited:
                    stk.append(nei)
        
        return True if len(visited)==len(rooms) else False



            
        