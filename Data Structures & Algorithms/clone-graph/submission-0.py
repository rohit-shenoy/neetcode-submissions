"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}

        def dfs(node):  # or clone
            if node in old_to_new:
                # don't create new Node, return already created copy
                return old_to_new[node]

            copy = Node(val=node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(
                    dfs(nei)
                )  # dfs nei creates and returns the copy, you add it to this nodes neighbors
            return copy
            
        return dfs(node)