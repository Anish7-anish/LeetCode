from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D = defaultdict(list)

        for u, v in prerequisites:
            D[u].append(v)
        print(D)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses


        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            elif state == VISITING: return False
            
            states[node] = VISITING

            for nei in D[node]:
                if not dfs(nei):
                    return False
                
            states[node] = VISITED
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True




        
        
        

        