# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = [False]
        def dfs(root,tsum,targetSum):
            if not root:
                return
            tsum+=root.val
            if not root.left and not root.right:
                if tsum == targetSum:
                    pathSum[0] = True
            dfs(root.left,tsum,targetSum)
            dfs(root.right,tsum,targetSum)
        dfs(root,0,targetSum)
        return pathSum[0]

        