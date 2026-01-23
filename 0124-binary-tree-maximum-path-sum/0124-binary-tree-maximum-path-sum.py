# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # # BFS 
        # q = [] 

        # self.max_sum = float('-inf')
        # val = 0
        # def levelOrder(root,level, val):
        #     if root is None:  
        #         val = 0
        #         return 
        #     print(root.val)
        #     val += root.val
        #     self.max_sum = max(self.max_sum, val)
        #     print('this is sum', self.max_sum)
        #     levelOrder(root.left, level + 1, val)
        #     levelOrder(root.right, level + 1, val)
            
            
        # levelOrder(root, 0, val)
        # return self.max_sum

        # left -> root -> right 

        if not root:
            return 
        queue = deque([root])
        result = []
        val = 0
        max_sum = float('-inf') 
        while queue:
            currentNode = queue.popleft()
            result.append(currentNode.val)
            val += currentNode.val

            if currentNode.left:
                queue.append(currentNode.left)
                val += currentNode.left.val
            if currentNode.right:
                queue.append(currentNode.right)
                val += currentNode.right.val
            max_sum = max(val, max_sum)
            val = 0
        return max_sum
            
