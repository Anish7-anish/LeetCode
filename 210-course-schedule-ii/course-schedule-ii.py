class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order =[]
        D = defaultdict(list)

        for u, v in prerequisites:
            D[u].append(v)
        

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses


        def dfs(node):
            
            if states[node] == VISITING: return False
            elif states[node] == VISITED : return True
            
            states[node] = VISITING

            for nei in D[node]:
                if not dfs(nei):
                    return False
                
            states[node] = VISITED
            order.append(node)
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order