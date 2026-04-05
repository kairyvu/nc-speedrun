class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.end = k - 1
        self.start = 0
        self.cap = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.end = (self.end + 1) % self.cap
        self.queue[self.end] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.start] = -1
        self.start = (self.start + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.start]

    def Rear(self) -> int:
        return self.queue[self.end]

    def isEmpty(self) -> bool:
        return self.size == 0        

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()