# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # if no root exists return the empty list
        if not root:
            return res
        queue = deque([root])
        level = 1

        # while there are elements in the queue
        while queue:
            levels = []
            # loop though all the elements currently in queue
            for _ in range(len(queue)):
                # get a node
                node = queue.popleft()
                # add the node to the levels list
                levels.append(node.val)
                # check the left child of the node
                if node.left:
                    queue.append(node.left)
                # check the right child of the node
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                levels.reverse()
                res.append(levels)
            else:
                res.append(levels)
            level += 1
        
        return res
