# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # queue initially has root - [1]
        q = collections.deque([root])
        result = []

        while q:
            
            levelList = []
            # snapshot of every level one at a time
            for i in range(len(q)):
                node = q.popleft()
                levelList.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(levelList)

        return result
