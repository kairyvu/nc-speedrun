class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        obtainable = [-1] * 3
        x1, y1, z1 = target

        for x, y, z in triplets:
            if x > x1 or y > y1 or z > z1:
                continue
            obtainable[0] = max(obtainable[0], x)
            obtainable[1] = max(obtainable[1], y)
            obtainable[2] = max(obtainable[2], z)
        
        return obtainable == target