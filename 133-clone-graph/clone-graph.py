"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        graph = {}
        seen = set()
        def dfs(node,seen):
            if node is None:
                return
            cur_node = Node(node.val)
            graph[node] = cur_node
            if node.neighbors is not None:
                for nei in node.neighbors:
                    if nei not in seen:
                        seen.add(nei)
                        dfs(nei,seen)

        dfs(node,seen)

        for key,val in graph.items():
            for nei in key.neighbors:
                nei_node = graph[nei]
                val.neighbors.append(nei_node)
        
        return graph[node]


        