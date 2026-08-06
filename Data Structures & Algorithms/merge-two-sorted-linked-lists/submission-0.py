# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = list3 = ListNode()
        while list1 and list2:
            # check if the head of list1 is less than the head of list2
            if list1.val < list2.val:
            # add the head of list1 to the mergedList
                list3.next = list1
            # increment the head of list1 to head.next
                list1 = list1.next

            else:
                list3.next = list2
                list2 = list2.next
            
            list3 = list3.next
        if list1:
            list3.next = list1
        else:
            list3.next = list2

        return mergedList.next
