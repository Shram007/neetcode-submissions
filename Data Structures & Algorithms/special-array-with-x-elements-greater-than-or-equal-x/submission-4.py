class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        totalRight = len(nums)
        prev = -1
        while i < len(nums):
            if nums[i] == totalRight or (prev < totalRight < nums[i]):
                return totalRight
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            prev = nums[i]
            i += 1
            totalRight = len(nums) - i
        return -1
