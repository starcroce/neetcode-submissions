from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.point_cnt = defaultdict(int)
        self.point_list = []

    def add(self, point: List[int]) -> None:
        self.point_list.append(point)
        self.point_cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.point_list:
            if abs(x - px) != abs(y - py):
                continue
            if x == px or y == py:
                continue
            res += self.point_cnt[(x, py)] * self.point_cnt[(px, y)]
        return res