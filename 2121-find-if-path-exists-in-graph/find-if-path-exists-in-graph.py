class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d = defaultdict(list)

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        seen = set()
        stk = [source]

        while stk:
            node = stk.pop()
            if node == destination:
                print('hi')
                return True
            
            for nei_node in d[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stk.append(nei_node)
                    
        return False
        