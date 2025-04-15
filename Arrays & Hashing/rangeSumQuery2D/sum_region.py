from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum_arr = [[0 for i in range (len(matrix[0])+1)] for j in range (len(matrix)+1)]
        
        for row in range(len(matrix)):
            row_sum = 0
            for col in range(len(matrix[0])):
                row_sum += matrix[row][col]
                self.prefix_sum_arr[row+1][col+1] = self.prefix_sum_arr[row][col+1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left_sum = self.prefix_sum_arr[row2+1][col1]
        upper_sum = self.prefix_sum_arr[row1][col2+1]
        extra_sum = self.prefix_sum_arr[row1][col1]

        return self.prefix_sum_arr[row2+1][col2+1] - left_sum - upper_sum + extra_sum