# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0

        # Returns height
        def dfs(curr: TreeNode):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal max_height
            max_height = max(max_height, left + right)

            return 1 + max(left, right)

        dfs(root)
        return max_height