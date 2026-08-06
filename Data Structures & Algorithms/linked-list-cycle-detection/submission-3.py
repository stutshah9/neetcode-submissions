# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer approach
        # loop while both the fast pointer and the node after the fast pointer exist
        # is the value of the fast and slow pointer equal each other return true --> the logic is like a fast runner catching up and lapping the slow runner while running on a track because it is a cycle
        # fast pointer increments by 2 whereas slow pointer increments by 1
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
            


