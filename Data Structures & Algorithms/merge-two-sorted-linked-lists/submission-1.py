# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy here will always be the head of the list
        # list3 is the tail which moves
        dummy = list3 = ListNode()

        while list1 and list2:
            # check if list1 is less than list2
            if list1.val < list2.val:
            # add list1 to the list3
                list3.next = list1
            # increment list1 to list1.next
                list1 = list1.next

            else:
                list3.next = list2
                list2 = list2.next
            
            list3 = list3.next
        if list1:
            list3.next = list1
        else:
            list3.next = list2

        return dummy.next
