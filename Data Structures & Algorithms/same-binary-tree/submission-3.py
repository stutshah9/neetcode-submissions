# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use BFS to recursively go through the trees
        # the trees must hold a node with the same value in the same place
        # if both are empty return true
        # if one is empty but the other is not return false

        if not p and not q:
            return True
        
        if (p and not q) or (not p and q):
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)