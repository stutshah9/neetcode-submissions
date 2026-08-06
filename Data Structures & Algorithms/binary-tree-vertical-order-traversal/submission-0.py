# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # dictionary where the key is the column and the value is a list of notes
        dict = defaultdict(list)
        q = deque([(root, 0)])    # (node, col)

        maxCol = 0
        minCol = 0

        output = []

        while q:
            # pop each node from the list
            node, col = q.popleft()
            # uodate the max and min col
            maxCol = max(maxCol, col)
            minCol = min(minCol, col)

            # append the current nodes value to the correct col
            dict[col].append(node.val)

            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
            
        for i in range(minCol,maxCol+1):
            output.append(dict[i])
        
        return output
            

