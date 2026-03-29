class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited or target in visited:
            return -1
        q = deque(["0000"])
        visited.add("0000")
        turns = 0

        while q:
            turns += 1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for diff in [1, -1]:
                        digit = str((int(lock[i]) + diff + 10) % 10)
                        newLock = lock[:i] + digit + lock[i+1:]
                        if newLock == target:
                            return turns
                        if newLock in visited:
                            continue
                        q.append(newLock)
                        visited.add(newLock)
        
        return -1