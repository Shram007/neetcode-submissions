class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0: return 1
            half = helper(x, n // 2)
            return half * half if n%2 == 0 else half * half * x
        result = helper(abs(x), abs(n))
        return result if n >= 1 else 1 / result
