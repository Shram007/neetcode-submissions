class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        res = []
        for num in freq:
            if freq[num] > len(nums) // 3:
                res.append(num)
        return res