class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self._sum_of_square(n)
            if n == 1:
                return True
        return False

    def _sum_of_square(self, n):
        res = 0
        while n:
            d = n % 10
            res += d ** 2
            n = n // 10
        return res