class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                res.append(matrix[i][j])
        l, r = 0, len(res) - 1
        while l <= r:
            m = l + (r - l) // 2
            if res[m] == target: return True
            elif res[m] < target: l = m + 1
            else: r = m - 1
        return False
