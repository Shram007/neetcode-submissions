class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        prod = 1
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1: return [0] * len(nums)
        
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            if zero_cnt == 1: res[i] = 0 if num else prod
            else: res[i] = prod // num
        return res
            


        