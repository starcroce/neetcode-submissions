class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            n = i
            while n:
                res[i] += 1
                n &= n - 1
        return res