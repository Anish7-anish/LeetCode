from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        D = defaultdict(list)

        for u, v in edges:
            D[u].append(v)
            D[v].append(u)

        seen = set()
        seen.add(source)

        l=[0]

        if n == 1 and source == destination:
            return True

        def dfs(node, destination):
            
            for nei in D[node]:
                if nei not in seen:
                    seen.add(nei)
                    
                    if destination in seen:
                        l[0] = 1
                        break
                        
                    dfs(nei, destination)

        dfs(source, destination)
        if l[0] == 1:
            return True
        return False



        