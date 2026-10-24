# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        def dfs(node):
            if not node:
                return None
            
            # swap children
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            # recursively invert those children 
            dfs(node.left)
            dfs(node.right)
            return node

        return dfs(root)