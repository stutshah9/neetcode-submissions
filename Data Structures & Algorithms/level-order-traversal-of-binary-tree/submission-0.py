# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # have a queue that stores the nodes
        queue = collections.deque()
        # add the root to the queue
        queue.append(root)
        # while the queue is empty
        while queue:
            # have a list for each level
            level = []
            # for the number of elements currently in the queue
            # nodes for that level
            for i in range(len(queue)):
                # pop the left most element out
                node = queue.popleft()
                # if it exists
                if node:
                    # add the node to the level list
                    level.append(node.val)
                    # add the left and right children of that node into the queue
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res

