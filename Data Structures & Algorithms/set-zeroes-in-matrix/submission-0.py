class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        first_row, first_col = False, False

        for i in range(row):
            if matrix[i][0] == 0:
                first_col = True
                break
        
        for j in range(col):
            if matrix[0][j] == 0:
                first_row = True
                break

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row:
            for j in range(col):
                matrix[0][j] = 0
        if first_col:
            for i in range(row):
                matrix[i][0] = 0