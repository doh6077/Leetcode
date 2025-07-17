# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # basically we have to check if the left node is less than the root node and the right node is greater than the root node 
        # DFS, recursive 

        # Base Case - when the node is empty 

        def valid(node, left, right):
            if not node:
                return True
            if not(node.val > left and node.val < right):
                return False 
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))
            




                
                    


        