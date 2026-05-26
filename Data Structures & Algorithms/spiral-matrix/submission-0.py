class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) # ROWS
        n = len(matrix[0]) # COLS

        res = []
        def recursive(row, col, r, c, dr, dc):
            if row == 0 or col == 0:
                return 
            
            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])

            recursive(col, row - 1, r, c, dc, -dr)

        recursive(m, n, 0, -1, 0, 1)
        return res