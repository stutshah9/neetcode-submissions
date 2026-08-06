# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # check if the node is null as the base case
        # have a maximum count
        # recursive approach

        maximumDepth = 0
        if not root:
            return 0

        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            maximumDepth = max(leftDepth, rightDepth)
            maximumDepth += 1

        return maximumDepth