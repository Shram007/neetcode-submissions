class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        n = len(nums)
        while l <= n - k:
            res.append(max(nums[l : k + l]))
            l += 1
        return res
            