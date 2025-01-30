class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        courses = prerequisites

        for a,b in courses:
            g[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED]*numCourses
        order = []
        
        def dfs(node):
            if states[node] == VISITED:
                return True
            elif states[node] == VISITING:
                return False
            
            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            order.append(node)
            return True
            
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order