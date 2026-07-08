class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ''' 
        res = nums[:]
        min_heap = [(num, i) for i, num in enumerate(nums)]

        heapq.heapify(min_heap)
        for _ in range(k):
            num, i = heapq.heappop(min_heap)
            res[i] *= multiplier
            heapq.heappush(min_heap, (res[i], i))
        return res 
        '''
        min_heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(min_heap)
        for _ in range(k):
            val, idx = heapq.heappop(min_heap)
            new_val = val * multiplier
            nums[idx] = new_val
            heapq.heappush(min_heap, (new_val, idx))
        return nums