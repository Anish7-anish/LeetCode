"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque()
        q.append(root)

        while q:
            level = []
            n = len(q)

            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.children: 
                    for n in node.children:
                        q.append(n)
            ans.append(level)
        return ans