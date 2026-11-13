# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def isBalancedAndHeight(node) -> Tuple(bool, int):
            # base case
            if not node:
                return (True, 0)

            leftBalHeight, rightBalHeight = isBalancedAndHeight(
                node.left
            ), isBalancedAndHeight(node.right)
            balanced = (
                leftBalHeight[0]
                and rightBalHeight[0]
                and (abs(leftBalHeight[1] - rightBalHeight[1]) <= 1)
            )

            return (balanced, 1 + max(leftBalHeight[1], rightBalHeight[1]))

        return isBalancedAndHeight(root)[0]
            
