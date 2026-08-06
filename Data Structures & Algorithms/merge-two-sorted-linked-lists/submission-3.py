# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity: O(n + m)
        # space complexity: O(1)
        # create a dummy node
        # loop while neither of the values that are being comapred is none
        # check which value from the list is smaller and have the last node that was added point to that node
        # if the first list has become none, add the remaining values from the second list to the result
        # if the second list has become none, add the remaining values from the first list to the result

        dummy = ListNode()
        compareResult = dummy

        curr1 = list1
        curr2 = list2

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                compareResult.next = curr1
                curr1 = curr1.next
            else:
                compareResult.next = curr2
                curr2 = curr2.next
            
            compareResult = compareResult.next
            
        if curr1 == None:
            compareResult.next = curr2
            
        if curr2 == None:
            compareResult.next = curr1
        
        return dummy.next
        