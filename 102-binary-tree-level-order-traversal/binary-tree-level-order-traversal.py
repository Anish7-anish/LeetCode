# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        que = deque([root])
        while que:
            size = len(que)
            level = []
            for i in range(size):
                node = que.popleft()
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
                level.append(node.val)
            ans.append(level)
        
        return ans
        