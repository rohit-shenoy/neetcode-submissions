# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        if not root:
            return output
        
        # Algorithm - [[], [2, 3], [4, 5, 6, 7]]
        # BFS with sub-list for a level, starting with root with deque

        q = collections.deque([root])

        while q:
            levelList = []
            
            # build the level
            for i in range(len(q)):
                node = q.popleft()
                levelList.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            output.append(levelList)
        
        return output




