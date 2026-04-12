class Node:
    def __init__(self, key, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
    
    def getLength(self):
        return len(self.map)
    
    def pushback(self, key):
        newNode = Node(key, self.tail, self.tail.prev)
        prevNode = self.tail.prev
        prevNode.next = newNode
        self.tail.prev = newNode
        self.map[key] = newNode
    
    def remove(self, key):
        if key in self.map:
            node = self.map[key]
            prevNode, nextNode = node.prev, node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.map.pop(key, None)
    
    def popleft(self):
        nodeKey = self.head.next.key
        self.remove(nodeKey)
        return nodeKey

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minF = 0
        self.keyToVal = {}
        self.keyToCount = {}
        self.countToList = defaultdict(LinkedList)

    def _counter(self, key):
        count = self.keyToCount[key]
        self.countToList[count].remove(key)
        if count == self.minF and self.countToList[count].getLength() == 0:
            self.minF += 1
        self.countToList[count + 1].pushback(key)
        self.keyToCount[key] += 1

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1
        self._counter(key)

        return self.keyToVal[key]     

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.keyToVal:
            self._counter(key)
        else:
            if len(self.keyToVal) == self.capacity:
                removeKey = self.countToList[self.minF].popleft()
                self.keyToVal.pop(removeKey, None)
                self.keyToCount.pop(removeKey, None)

            self.keyToCount[key] = 1
            self.minF = 1
            self.countToList[self.keyToCount[key]].pushback(key)
        self.keyToVal[key] = value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)