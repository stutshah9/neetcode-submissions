"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # in the first pass
        # create a copy of the nodes without any of the next and random pointers
        # have a hashmap to map the original nodes to the copy
        # in the second pass loop at the hashmap and the copied node
        # add the right pointer connections into the nodes

        # first pass
        curr1 = head
        # key = original node
        # value = copied node
        nodeCopyDict = {}

        while curr1:
            # create a new node
            newNode = Node(curr1.val)
            # save to the hashmap
            nodeCopyDict[curr1] = newNode
            curr1 = curr1.next
        
        # second pass
        # loop over he linked list again
        # check where the next and random pointer point to
        # find the copies of those nodes in the hashmap and make the pointers of the copies point to them
        curr2 = head
        while curr2:
            nextPointer = curr2.next
            randomPointer = curr2.random

            copyNode = nodeCopyDict[curr2]
            nextNode = None
            randomNode = None

            if randomPointer:
                randomNode = nodeCopyDict[curr2.random]
            
            if nextPointer:
                nextNode = nodeCopyDict[curr2.next]

            copyNode.next = nextNode
            copyNode.random = randomNode

            curr2 = curr2.next
    
        return nodeCopyDict[head]