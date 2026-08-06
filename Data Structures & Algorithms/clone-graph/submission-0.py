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

        oldToNew = defaultdict(Node)

        def clone(node):
            # if the clone is already made
            if node in oldToNew:
                # return the clone
                return oldToNew[node]
            
            # make a copy of the node
            copy = Node(node.val)
            # add it to the dictionary
            oldToNew[node] = copy
            # for each neighbor the node has
            for nei in node.neighbors:
                # add the clones of the neighbors as neighbors
                copy.neighbors.append(clone(nei))
            return copy
        return clone(node)
