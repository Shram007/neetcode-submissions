class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                height = min(heights[i], heights[j])
                width = j - i
                area = height * width
                res = max(res, area)
        return res
