import math

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row, col = len(matrix), len(matrix[0])
        for i in range(min(math.ceil(row / 2), math.ceil(col / 2))):
            print(i)
            for val in self._get_edges(matrix, i):
                res.append(val)
        return res

    def _get_edges(self, matrix, level):
        res = []
        row, col = len(matrix), len(matrix[0])

        if level == row - 1 - level:
            for i in range(level, col - level):
                res.append(matrix[level][i])
            return res
        
        if level == col - 1 - level:
            for i in range(level, row - level):
                res.append(matrix[i][level])
            return res

        for i in range(level, col - 1 - level):
            res.append(matrix[level][i])
        for i in range(level, row - 1 - level):
            res.append(matrix[i][col-1-level])
        for i in range(col - 1 - level, level, -1):
            res.append(matrix[row-1-level][i])
        for i in range(row - 1 - level, level, -1):
            res.append(matrix[i][level])
        return res