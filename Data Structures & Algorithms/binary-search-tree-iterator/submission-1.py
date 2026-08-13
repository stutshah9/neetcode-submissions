# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.root = root
    #     self.result = []
    #     self.inOrder(root, self.result)
    #     self.pointer = -1

    # # move to get the next value
    # def next(self) -> int:
    #     self.pointer += 1
    #     return self.result[self.pointer]

    # # is there another value
    # def hasNext(self) -> bool:
    #     if self.pointer + 1 < len(self.result):
    #         return True
    #     return False
    

    # def inOrder(self, root, result):
    #     if root:
    #         # visit everything on the left
    #         self.inOrder(root.left, self.result)
    #         # record the current node
    #         self.result.append(root.val)
    #         # visit everything on the right
    #         self.inOrder(root.right, self.result)

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    # move to get the next value
    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    # is there another value
    def hasNext(self) -> bool:
        return self.stack != []



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()