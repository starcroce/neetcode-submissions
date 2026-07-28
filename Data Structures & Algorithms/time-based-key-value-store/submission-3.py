class TimeMap:

    def __init__(self):
        self.store_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store_map[key] = self.store_map.get(key, [])
        self.store_map[key].append((value, timestamp))
        print(self.store_map)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store_map:
            return ""
        values = self.store_map[key]
        start, end = 0, len(values) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if values[mid][1] <= timestamp:
                start = mid
            else:
                end = mid
        # print(values[start], values[end])
        if values[end][1] <= timestamp:
            return values[end][0]
        elif values[start][1] <= timestamp:
            return values[start][0]
        else:
            return ""
