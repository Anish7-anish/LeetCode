# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        in_order_arr = []
        def in_order(root):
            if not root:
                return 
            
            in_order(root.left)
            in_order_arr.append(root.val)
            in_order(root.right)
        in_order(root)
        
        left = 0
        right = 1
        min_diff = float('inf')
        while right < len(in_order_arr):
            min_diff = min(min_diff,abs(in_order_arr[left]-in_order_arr[right]))
            left+=1
            right+=1
        return min_diff
