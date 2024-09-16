"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        stk = [start]
        visited = set()
        visited.add(start)
        o_to_n = {}

        while stk:
            node = stk.pop()
            o_to_n[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)

        for old_node , new_node in o_to_n.items():
            for nei in old_node.neighbors:
                nei_node = o_to_n[nei]
                new_node.neighbors.append(nei_node)

        return o_to_n[start]

        

        

        