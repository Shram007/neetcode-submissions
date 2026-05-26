class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ''' n = len(nums)
        sums = (n * (n + 1)) // 2
        res = 0
        for i in nums:
            res += i
        return sums - res '''

        # more optimal sol

        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res