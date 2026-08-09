# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # starting at the top node
        # if node.val is greater than the key, serach the left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if node.val is less than the key, serach the right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # if it is equal you have found the key
        else:
            # no left child
            if not root.left:
                return root.right

            # no right child
            if not root.right:
                return root.left

            # two children
            successor = root.right

            while successor.left:
                successor = successor.left
            
            root.val = successor.val

            # delete the orgiginal successor node
            root.right = self.deleteNode(root.right, successor.val)

        return root
        