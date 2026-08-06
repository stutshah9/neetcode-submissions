# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # have a queue which keeps account of the root nodes
        # swap the left and right nodes of the root node currently dealing with
        # process the children and check if any of them are leaf nodes
        # if they are leaf nodes swap them but do not add them to the queue

        queue = deque()
        queue.append(root)

        if not root:
            return root
        
        while queue:
            currRoot = queue.popleft()
            temp = currRoot.right
            currRoot.right = currRoot.left
            currRoot.left = temp

            rightCurr = currRoot.right
            leftCurr = currRoot.left

            if rightCurr:
                queue.append(rightCurr)
            
            if leftCurr:
                queue.append(leftCurr)
        
        return root
        