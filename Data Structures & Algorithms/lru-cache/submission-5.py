class Node:
    def __init__(self, key, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.keyToNode = {}
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    
    def _addToEnd(self, node):
        lastNode = self.tail.prev
        lastNode.next = node
        node.prev = lastNode
        node.next = self.tail
        self.tail.prev = node
    
    def _removeNode(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        return node.key

    def get(self, key: int) -> int:
        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]
        self._removeNode(node)
        
        self._addToEnd(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            self._removeNode(node)
            self._addToEnd(node)
            return

        newNode = Node(key, value)
        self._addToEnd(newNode)
        self.keyToNode[key] = newNode

        if len(self.keyToNode) > self.capacity:
            lru = self.head.next
            self._removeNode(lru)
            del self.keyToNode[lru.key]
