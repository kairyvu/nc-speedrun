class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                topSum = self.prefixSum[r - 1][c] if r > 0 else 0
                leftSum = self.prefixSum[r][c - 1] if c > 0 else 0
                dupSum = self.prefixSum[r - 1][c - 1] if r > 0 and c > 0 else 0
                self.prefixSum[r][c] = matrix[r][c] + topSum + leftSum - dupSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topSum = self.prefixSum[row1 - 1][col2] if row1 > 0 else 0
        leftSum = self.prefixSum[row2][col1 - 1] if col1 > 0 else 0
        dupSum = self.prefixSum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.prefixSum[row2][col2] - topSum - leftSum + dupSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)