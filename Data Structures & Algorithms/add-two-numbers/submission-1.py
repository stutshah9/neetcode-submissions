# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        # have a function to reverse the nodes of the list
        l1Reverse = self.reverseList(l1)
        l2Reverse = self.reverseList(l2)
        # function for:
        # while the node is not null
        # loop through and get the values of the node
        # get the values as strings so that they can be joined using '+'
        # then convert back to int
        num1 = self.numberList(l1Reverse)
        num2 = self.numberList(l2Reverse)

        # mathematically add the numbers together
        numResult = num1 + num2
        # convert the result to a string
        strResult = str(numResult)
        # loop through in reverse order and append to the result
        curr = head
        for i in range(len(strResult) - 1, -1, -1):
            newNode = ListNode(int(strResult[i]))
            
            if not head and not tail:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        
        return head

    def numberList(self, list: Optional[ListNode]) -> int:
        curr = list
        numberString = ""
        while curr:
            numberString = numberString + str(curr.val)
            curr = curr.next

        return int(numberString)
    
    def reverseList(self, list: Optional[ListNode]) -> Optional[ListNode]:
        if not list:
            return list
        
        prev = None
        curr = list
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev