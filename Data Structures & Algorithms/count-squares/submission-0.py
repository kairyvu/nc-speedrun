class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for k, v in list(self.points.items()):
            x, y = k
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += v * self.points[(x, py)] * self.points[(px, y)]
        return res
