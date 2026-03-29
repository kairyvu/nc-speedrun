class MyHashSet:

    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]

    def _getBucket(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        index = self._getBucket(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self._getBucket(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._getBucket(key)
        return key in self.buckets[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)