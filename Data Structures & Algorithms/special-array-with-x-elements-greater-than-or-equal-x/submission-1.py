class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(0, n + 1):
            cnt = sum(1 for num in nums if num >= x)
            if cnt == x: return x
        return -1