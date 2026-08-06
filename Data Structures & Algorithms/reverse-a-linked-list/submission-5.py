# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity: O(n)
        # space complexity: O(1)
        # use a prev pointer
        # while head.next is not NULL
        # point the head.next to the prev pointer
        # move the prev to the head and the head to head.next

        prev = None
        while head != None:
            tempNext = head.next
            head.next = prev
            prev = head
            head = tempNext
        
        return prev
