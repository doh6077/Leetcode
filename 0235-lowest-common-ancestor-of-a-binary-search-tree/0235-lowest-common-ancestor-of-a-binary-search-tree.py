# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        stack1 = [] 
        stack2 = []

        

        def find(root,stack, lookval):
            while root:
                stack.append(root)
                if root.val != lookval.val:
                    
                    if lookval.val > root.val:
                        root = root.right
                    else:
                        root = root.left 

                else:
                    return stack 
        
        stack1 = find(root,stack1, p)
        stack2 = find(root,stack2, q)
        ans = [i for i, j in zip(stack1, stack2) if i == j]
        return ans[-1] if ans else root



    

        