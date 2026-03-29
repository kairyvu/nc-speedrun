class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        counter = [(-count, key) for key, count in counter.items()]
        heapq.heapify(counter)

        res = []
        while counter:
            count1, ch1 = heapq.heappop(counter)
            count1 += 1
            if count1 < 0 and not counter:
                return ""
            res.append(ch1)
            if counter:
                count2, ch2 = heapq.heappop(counter)
                count2 += 1
                res.append(ch2)
                if count2:
                    heapq.heappush(counter, (count2, ch2))
            if count1:
                heapq.heappush(counter, (count1, ch1))
        
        return "".join(res)