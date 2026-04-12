class ListNode:
    def __init__(self, key, value=0, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0, prev=self.head)
        self.head.next = self.tail
    
    def updateNode(self, key, value):
        node = self.find(key)
        if not node:
            lastNode = self.tail.prev
            newNode = ListNode(key, value, self.tail, lastNode)
            lastNode.next = newNode
            self.tail.prev = newNode
        else:
            node.value = value
    
    def remove(self, key):
        node = self.find(key)
        if not node:
            return
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def find(self, key):
        curr = self.head.next
        while curr != self.tail:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

class MyHashMap:

    def __init__(self):
        self.bucket = 1000
        self.store = [LinkedList()] * self.bucket
    
    def _getBucket(self, key):
        return key % self.bucket

    def put(self, key: int, value: int) -> None:
        index = self._getBucket(key)
        self.store[index].updateNode(key, value)

    def get(self, key: int) -> int:
        index = self._getBucket(key)
        node = self.store[index].find(key)
        return -1 if not node else node.value

    def remove(self, key: int) -> None:
        index = self._getBucket(key)
        self.store[index].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)