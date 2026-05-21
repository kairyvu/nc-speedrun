class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            currPrefix = 0
            for c in range(cols):
                topRegion = self.sumMatrix[r - 1][c] if r > 0 else 0
                currPrefix += matrix[r][c]
                self.sumMatrix[r][c] = currPrefix + topRegion
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topRegion = self.sumMatrix[row1 - 1][col2] if row1 > 0 else 0
        leftRegion = self.sumMatrix[row2][col1 - 1] if col1 > 0 else 0
        overlap = self.sumMatrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.sumMatrix[row2][col2] - topRegion - leftRegion + overlap



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)