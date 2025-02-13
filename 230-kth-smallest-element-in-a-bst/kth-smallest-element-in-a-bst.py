# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [0]
        count = [k]
        def in_order(root):
            if not root:
                return
            
            in_order(root.left)

            if count[0] == 1:
                ans[0] = root.val

            count[0] = count[0]-1
            
            if count[0]>0:
                in_order(root.right)
        in_order(root)

        return ans[0]
        
        

        