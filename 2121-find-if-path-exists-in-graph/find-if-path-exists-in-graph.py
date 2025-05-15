from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)

        seen = set()
        stack = []
        stack.append(source)

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in d[node]:
                if nei_node not in seen:
                    stack.append(nei_node)
                    seen.add(nei_node)
        
        return False


        