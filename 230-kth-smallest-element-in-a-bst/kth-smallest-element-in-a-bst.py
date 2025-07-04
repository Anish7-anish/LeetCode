# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def in_order(root):
            if not root:
                return
            in_order(root.left)
            ans.append(root.val)
            in_order(root.right)
        
        in_order(root)
        return ans[k-1]
        