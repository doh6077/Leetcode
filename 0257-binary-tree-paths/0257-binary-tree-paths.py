# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        ans = []
        def dfs(node, path):
            if not node:
                return 
            path += str(node.val)
            if not node.right and not node.left:
                ans.append(path)
            else:
                dfs(node.right, path + "->")
                dfs(node.left, path + "->" )
        
        dfs(root, "")
        return ans
        



        