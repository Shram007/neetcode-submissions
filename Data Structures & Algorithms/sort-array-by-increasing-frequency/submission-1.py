class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
