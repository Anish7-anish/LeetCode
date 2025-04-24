# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        order = []
        def in_order(root):
            if not root:
                return
            
            in_order(root.left)
            order.append(root.val)
            in_order(root.right)
        
        in_order(root)
        
        a = 0
        b = 1
        
        min_diff = float('inf')
        while b < len(order):
            cur_diff = abs(order[a] - order[b])
            min_diff = min(min_diff, cur_diff)
            a+=1
            b+=1
        
        return min_diff
        