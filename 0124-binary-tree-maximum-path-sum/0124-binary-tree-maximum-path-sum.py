# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]

        def dfs(root):


            if root is None:
                return 0 
                
            leftVal = dfs(root.left)
            rightVal = dfs(root.right)
            leftVal = max(leftVal, 0)
            rightVal = max(rightVal, 0)

            res[0] = max(res[0], root.val + rightVal + leftVal)
            
            return root.val + max(leftVal, rightVal)
        dfs(root)
        return res[0]