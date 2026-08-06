# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        node = head
        # while the node
        while node:
        # if the set already contains the node
            if node in nodeSet:
        # return true
                return True
        # else move to the next node
            else:
                # add node to set
                nodeSet.add(node)
                node = node.next
        return False