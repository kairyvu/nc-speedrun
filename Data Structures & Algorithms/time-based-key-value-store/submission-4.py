class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append((timestamp, value))

    def _search_most_recent(self, arr, timestamp):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return arr[r][1] if 0 <= r < len(arr) else ""
        
    def get(self, key: str, timestamp: int) -> str:
        return self._search_most_recent(self.keyStore[key], timestamp)
