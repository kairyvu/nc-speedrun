class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        countAtPos = defaultdict(int)
        
        for psg, src, dst in trips:
            countAtPos[src] += psg
            countAtPos[dst] -= psg
        

        for key in sorted(countAtPos):
            capacity -= countAtPos[key]
            if capacity < 0:
                return False
        return True