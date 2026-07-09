class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        transpose = [[0] * ROWS for _ in range(COLS)]

        for i in range(ROWS):
            for j in range(COLS):
                transpose[j][i] = matrix[i][j]
        return transpose