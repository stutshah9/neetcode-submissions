# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result
        
        queue = deque()
        level = 1

        queue.append(root)
        result = []

        while queue:
            sizeQueue = len(queue)
            levelList = []
            for _ in range(sizeQueue):
                top = queue.popleft()
                levelList.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            result.append(levelList)
        
        return result