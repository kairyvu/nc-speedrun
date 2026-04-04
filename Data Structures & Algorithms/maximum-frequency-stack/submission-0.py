class FreqStack:

    def __init__(self):
        self.countToVal = defaultdict(list) # count -> list of val
        self.valCount = defaultdict(int) # val -> count
        self.maxF = 0

    def push(self, val: int) -> None:
        self.valCount[val] += 1
        self.countToVal[self.valCount[val]].append(val)
        self.maxF = max(self.maxF, self.valCount[val])

    def pop(self) -> int:
        value = self.countToVal[self.maxF].pop()
        if not self.countToVal[self.maxF]:
            self.maxF -= 1
        self.valCount[value] -= 1
        return value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()