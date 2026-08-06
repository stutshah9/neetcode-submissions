class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    from collections import defaultdict
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # remove the node from position
            node.prev.next = node.next
            node.next.prev = node.prev

            # add node before tail
            previousNode = self.tail.prev
            previousNode.next = node
            node.prev = previousNode
            node.next = self.tail
            self.tail.prev = node
            
        else:
            if self.size < self.capacity:
                self.add(key, value)
            else:
                # remove the first node
                self.remove()
                # add new node at the end
                self.add(key, value)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        # remove the node from position
        node.prev.next = node.next
        node.next.prev = node.prev

        # add node before tail
        previousNode = self.tail.prev
        previousNode.next = node
        node.prev = previousNode
        node.next = self.tail
        self.tail.prev = node

        return node.value

    def add(self, key: int, value: int) -> None:
        # add a node
        newNode = Node(key, value)
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail

        self.cache[key] = newNode
        self.size += 1
    
    def remove(self) -> None:
        nodeToRemove = self.head.next

        nextNode = nodeToRemove.next
        self.head.next = nextNode
        nextNode.prev = self.head

        del self.cache[nodeToRemove.key]
        self.size -= 1
