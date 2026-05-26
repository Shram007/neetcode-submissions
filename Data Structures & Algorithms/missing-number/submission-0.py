class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sums = (n * (n + 1)) // 2
        res = 0
        for i in nums:
            res += i
        return sums - res