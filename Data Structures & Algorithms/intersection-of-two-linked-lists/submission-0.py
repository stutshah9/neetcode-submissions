# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = self.getSize(headA)
        sizeB = self.getSize(headB)

        difference = abs(sizeA - sizeB)

        currA = headA
        currB = headB

        if sizeA > sizeB:
            for _ in range(difference):
                currA = currA.next

        if sizeB > sizeA:
            for _ in range(difference):
                currB = currB.next

        while currA:
            if currA == currB:
                return currA
            else:
                currA = currA.next
                currB = currB.next
        
        return None
    
    def getSize(self, head):
        count = 0
        current = head

        while current:
            count += 1
            current = current.next
        
        return count