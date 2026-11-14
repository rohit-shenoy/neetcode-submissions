# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        # t is non-empty
        if not s:
            return False

        if self.isSameTree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif q and not p:
            return False

        return (
            (p.val == q.val)
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
            )