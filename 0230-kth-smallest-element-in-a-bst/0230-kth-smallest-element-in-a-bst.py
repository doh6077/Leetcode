# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # This will hold the answer when found
        self.k = k
        self.result = None
        
        # In-order traversal
        def inorder(node):
            if not node:
                return
            
            # Visit the left child first
            inorder(node.left)
            
            # Now visit the node itself
            self.k -= 1  # Decrease k for each node visited
            
            if self.k == 0:  # If we've found the kth smallest, store it
                self.result = node.val
                return
            
            # If not found yet, visit the right child
            inorder(node.right)
        
        # Start the in-order traversal
        inorder(root)
        
        # Return the result once we've found the kth smallest
        return self.result
