# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # new linked list with dummy node as head
        # result points to the tail of the linked list
        dummy = result = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0

            if l2:
                v2 = l2.val
            else:
                v2 = 0
            
            total = v1 + v2 + carry
            # to calculate carry
            carry = total//10
            # to calculate the digit
            total = total % 10
            result.next = ListNode(total)

            result = result.next

            if l1:
                l1 = l1.next
            else:
                None
            if l2:
                l2 = l2.next
            else:
                None
        return dummy.next